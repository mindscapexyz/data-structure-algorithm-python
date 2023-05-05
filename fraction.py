def gcd(m, n):
    # Greatest common divisor: Euclid's Algorithm
    # Only works if denominator is positive

    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n

    return n


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
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num + other.den
        second_num = other.num + self.den

        return first_num == second_num


my_f = Fraction(1, 2)
print(my_f)
my_f_s = Fraction(1, 2)
sum_f = my_f + my_f_s

print(sum_f)

print(my_f == my_f_s)
