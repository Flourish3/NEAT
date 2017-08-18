# connect_gene.pt

class connect_gene:

    def __init__(self, input_node, out, weight, enabled, innovation):
        self.input_node = input_node
        self.output_node = out
        self.weight = weight
        self.enabled = enabled
        self.innovation = innovation
    def __repr__(self):
        return 'Input node: {}, output node: {}, connection weight: {}, enabled: {}, innovation number: {}'.format(self.input_node, self.output_node, self.weight, self.enabled, self.innovation)
