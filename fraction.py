class Fraction:
    """Class to represent fraction data structure"""

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


my_f = Fraction(3, 5)
print(my_f)
