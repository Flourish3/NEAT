#Configuration class to keep track of configuration in the network

class config:
    def __init__(self):
        self.compatability_constants = [1, 1, 0.4]
        self.compatability_distance = 3
        self.max_gen_without_improvement = 15
    
    def get_config(self):
        return {'compatability_constants' : self.compatability_constants, 'compatability_distance': self.compatability_distance, 
    'max_gen_without_improvement': self.max_gen_without_improvement }

    def set_config(self,c):
        self.compatability_constants     = c['compatability_constants']
        self.compatability_distance      = c['compatability_distance']
        self.max_gen_without_improvement = c['max_gen_without_improvement']
