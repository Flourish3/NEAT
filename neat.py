from genome.genome import Genome
from config import config

class NEAT:
    def __init__(self, inputs, outputs, population):
        self.inputs = inputs
        self.outputs = outputs
        self.population_nbr = population
        self.genome_list = []
        self.config = config()
        for i in range(population_nbr):
            genome_list.append(Genome(inputs,outputs,i))


    def get_next_genome(self):
        return self.genome_list[self.genome_index]
    
    def set_fitness(self, genome, fitness):
        self.genome_list[genome.index].fitness = fitness

    def progress_generation(self):
        
        speciate(genome_list)
        #Chose champions
        #mutate/evolve champions
        #check improvement
    
    def speciate(self):
        pass
    
    def generate_next_generation(self):
        pass

#Champion of each specie with more that five network would be copied to the next generation
#In that case -> 80% chance of having weights mutated
#   90% chance of being uniformely disturbed
#   10% och new random value
#75% chance that disabled gene would be disabled if that was the case for either parents
#25% of offspring from mutation without crossover
#Interspecies mating rate 0.1%
#New node 3% chance in mutation
#New connection 5% in mutation
#With larger population this number can be 30%