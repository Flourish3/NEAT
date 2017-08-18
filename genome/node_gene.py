import numpy as np

class node_gene:
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.output = 0
        self.is_recurrent = False

    def __repr__(self):
        return 'Node number {}, name: {}'.format(self.number,self.name)

    def calc_output(self):
        out = self.sigmoid(self.output)
        if not self.is_recurrent:
            output = 0
        return out

    def sigmoid(self,input_value):
        return 1/(1+np.exp(-4.9*input_value))

    def add_to_output(self,input_value):
        self.output += input_value

node = node_gene(1,'Input')
node.add_to_output(0.5)
print(node.calc_output())
