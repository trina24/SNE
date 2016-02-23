import gate

class Not(gate.Gate):
    
    def __init__(self):
        self.weights = [-0.3, 0.2]
