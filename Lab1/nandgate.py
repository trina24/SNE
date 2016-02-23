import gate

class Nand(gate.Gate):
    
    def __init__(self):
        self.weights = [-0.3, -0.4, 0.5]
