import math

class MyMathModule:
    def _init_(self, number):
        self.number = number
    
    def square(self):
        return self.number ** 2
    
    def square_root(self):
        return math.sqrt(self.number)
    
    def factorial(self):
        return math.factorial(self.number)
    
    def logarithm(self):
        return math.log(self.number)
    
   
    
class MyException(Exception):
    def init(self, message):
        self.message = message

    def msg(self):
        return self.message