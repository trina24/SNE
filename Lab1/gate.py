class Gate:

      def __init__(self):
            self.weights = []
      
      def scalar_product(self, vector):
            sum = 0
            for i in range(len(vector)):
                  sum += vector[i] * self.weights[i]
            return sum
      
      def neuron_function(self, vector):
            if (self.scalar_product(vector) >= 0):
                  return 1
            else:
                  return 0