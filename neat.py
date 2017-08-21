from genome.genome import Genome

#inputs = 3
#outputs = 1
compatability_constants = [1, 1, 0.4]
compatability_distance = 3
#population = 150
max_gen_without_improvement = 15

class neat:
    def __init__(self, inputs, outputs, population):
        self.inputs = inputs
        self.outputs = outputs
        self.population = population
        self.genome_list = []
        for _ in range(population):
            genome_list.append(Genome(inputs,outputs))
        self.fitness_list = []
        self.genome_index = 0

    def get_next_genome(self):
        return self.genome_list[self.genome_index]
    
    def set_fitness(self, fitness):
        self.fitness_list[self.genome_index] = fitness
        if self.genome_index < self.population:
            self.genome_index += 1
            return True
        else:
            self.genome_index = 0
            return False


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