class node_gene:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def __repr__(self):
        return 'Node number {}, name: {}'.format(self.number,self.name)

n1 = node_gene(1, 'Output')
