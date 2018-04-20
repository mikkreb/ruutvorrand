import math


class Square_equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.x1 = self.give_x1()
        self.x2 = self.give_x2()
        
    def give_x1(self):
        try:
            under_square_root = (self.b**2)-(4*self.a*self.c)
            square_root = math.sqrt(under_square_root)
            numerator = -1*self.b + square_root
            finalization = numerator / 2*self.a
            return(numerator / 2*self.a)
        except(ValueError):
            return("Lahendid puuduvad")

    def give_x2(self):
        try:
            under_square_root = (self.b**2)-(4*self.a*self.c)
            square_root = math.sqrt(under_square_root)
            numerator = -1*self.b - square_root
            finalization = numerator / 2*self.a
            return(numerator / 2*self.a)
        except(ValueError):
            return("Lahendid puuduvad")

print(Square_equation(2, 3, 4))
