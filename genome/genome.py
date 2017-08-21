#genome.py

from .node_gene import node_gene
from .connect_gene import connect_gene
from random import random

class Genome:
    
    def __init__(self, inputs, outputs):
        self.nbr_input = inputs
        self.nbr_output = outputs
        self.nbr_nodes = 0
        self.nodes = {}
        self.outputs = []
        self.connections = []
        self.innov = 0
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
        pass
    
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
        weight = self.generate_weight(1)
        self.connections.append(connect_gene(node1,node2,weight,innov))

    #Changes the weights on the connections in the genome
    def mutate_change_weights(self,mutation_chance):
        for conn in self.connections:
            if conn.enabled
                if random() < mutation_chance:
                    conn.weight += self.generate_weight(0.25)
                else:
                    conn.weight = self.generate_weight(1)
