import math

class AreaCalc:
    # TODO: Implement calculate method
    def __init__(self):
        pass
    def calculate(self,length: int, width: int=None):
        if width == None:
            return round(((math.pi)*length*length),2)
        else:
            return round(length*width,2)


    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
