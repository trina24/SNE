import gate

class Or(gate.Gate):
    
    def __init__(self):
        self.weights = [0.3, 0.4, -0.1]
