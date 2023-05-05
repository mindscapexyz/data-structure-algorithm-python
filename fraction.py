class Fraction:
    """Class to represent fraction data structure"""

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)


my_f = Fraction(3, 5)
print(my_f)
my_f_s = Fraction(1, 5)
sum_f = my_f + my_f_s
print(sum_f)
