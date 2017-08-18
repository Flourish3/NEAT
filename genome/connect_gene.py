# connect_gene.py

class connect_gene:

    def __init__(self, input_node, output_node, weight, enabled, innovation,accessed=False):
        self.input_node = input_node
        self.output_node = output_node
        self.weight = weight
        self.enabled = enabled
        self.innovation = innovation
        self.accessed = accessed
    def __repr__(self):
        return 'Input node: {}, output node: {}, connection weight: {}, enabled: {}, innovation number: {}, accessed: {}'.format(self.input_node, self.output_node, self.weight, self.enabled, self.innovation, self.accessed)
