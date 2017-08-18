import genome

inputs = 3
outputs = 1
compatability_constants = [1, 1, 0.4]
compatability_distance = 3
population = 150
max_gen_without_improvement = 15

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