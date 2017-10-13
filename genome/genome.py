#genome.py

from .node_gene import node_gene
from .connect_gene import connect_gene
from random import random

class Genome:
    
    def __init__(self, inputs, outputs, index, genes = None):
        self.nbr_input = inputs
        self.nbr_output = outputs
        self.nbr_nodes = 0
        self.nodes = {}
        self.outputs = []
        self.connections = []
        self.innov = 0
        self.fitness = 0
        self.index = index

        if genes == None:
            for _ in range(self.nbr_input):
                self.nodes[self.nbr_nodes] = node_gene(self.nbr_nodes,'Input')
                self.nbr_nodes += 1
            for _ in range(self.nbr_output):
                new_node = node_gene(self.nbr_nodes,'Output')
                self.nodes[self.nbr_nodes] = new_node
                self.outputs.append(new_node)
                self.nbr_nodes += 1
            for i in range(self.nbr_input):
                for j in range(self.nbr_output):
                    weight = self.generate_weight(1) 
                    self.connections.append(connect_gene(self.nodes[i], self.outputs[j], weight, True, self.innov))
                    self.innov += 1
        else:
            pass
            
    def generate_weight(self,range):
        return unform(-1*range,range) # Random weight between -range and range

    def propagate(self, input):
        #Check len(input == nbr_input)
        for j in range(self.nbr_input):
            self.nodes[j].add_to_output(input[j])
        
        for i in range(len(self.connections)):
            self.process_connection(self.connections[i],i)
        
        for conn in self.connections:
            conn.accessed = False

        output = []
        for out in self.outputs:
            output.append(out.calc_output())
        return output

    def process_connection(self, connection, index):
        if not connection.accessed or connection.enabled:
            self.check_input(connection,index)
            connection.output_node.add_to_output(connection.input_node.calc_output()*connection.weight)
            connection.accessed = True

    def check_input(self, connection, index):
        if connection.input_node.name == 'Input' or connection.input_node.is_recurrent:
            return
        else:
            for i in range(index,len(self.connections)):
                if self.connections(i).output_node == connection.input_node:
                    self.process_connection(self.connections(i), i)        

    def crossover(self, other):
        #Find matching genes
        connects = {}
        new_connections = []

        for conn in self.connections:
            connects[conn.innov] = 1
        for conn in other.connections:
            if conn.innov in connects:
                connects[conn.innov] += 1
            else:
                connects[conn.innov] = 3

        for k,v in connects:
            if v > 1:
                if random() < 0.5:
                    new_connections.append(self.connections[k])
                else:
                    new_connections.append(other.connections[k])
                del connects[k]
        
        if self.fitness > other.fitness:
            find_value = 1
        else:
            find_value = 3
    
        for k,v in connects:
            if v == find_value:
                new_connections.append(self.connections[k])

        #Create new genome with genes from self and other

    
    #Adds a new node, splitting an old, random connection
    def mutate_add_node(self,innov):
        mutate_connection = self.connections[random.randrange(len(self.connections))]
        mutate_connection.enabled = False

        self.nodes[self.nbr_nodes] = node_gene(self.nbr_nodes,"Hidden") 
        #Connection between previous input and new hidden        
        self.connections.apped(connect_gene(mutate_connection.input_node, self.nodes[self.nbr_nodes],1,innov))
        #Connection between hidden and previous output
        self.connections.append(connect_gene(self.nodes[self.nbr_nodes],mutate_connection.output_node, mutate_connection.weight,innov+1))

        self.nbr_nodes += 1

    #Adds a new connection between two random nodes
    def mutate_add_connection(self,innov):
        node1 = self.nodes[random.randrange(self.nbr_nodes)]
        node2 = self.nodes[random.randrange(self.nbr_nodes)]
        
        if node1 == node2:
            node1.is_recurrent = True
        
        weight = self.generate_weight(1)
        self.connections.append(connect_gene(node1,node2,weight,innov))

    #Changes the weights on the connections in the genome
    def mutate_change_weights(self,mutation_chance):
        for conn in self.connections:
            if conn.enabled:
                if random() < mutation_chance:
                    conn.weight += self.generate_weight(0.25)
                else:
                    conn.weight = self.generate_weight(1)
