__author__ = 'Rashed'


class Calculator:
    """Do addition, subtraction, multiplication and division."""

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'It is impossible to divide by zero.'

class SuperCalculator(Calculator):
    """Do addition, subtraction, multiplication, division, square and cube."""

    def addition(self, a, b, c):
        return a + b + c

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a

my_calculator = SuperCalculator()

temp = my_calculator.addition(23, 47, 12)
print(temp)

temp = my_calculator.subtraction(87, 54)
print(temp)

temp = my_calculator.multiplication(65, 56)
print(temp)

temp = my_calculator.division(852, 76)
print(temp)

temp = my_calculator.square(7)
print(temp)

temp = my_calculator.cube(3)
print(temp)