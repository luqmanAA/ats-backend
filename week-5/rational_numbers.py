

class RationalNumber:

    def __init__(self, numerator:int = 1, denominator:int = 2) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}" 

    def add_rational_number(self, other_rational_number):
        if not isinstance(other_rational_number, RationalNumber):
            return f"{other_rational_number} is not a fraction"
        return f"{self.numerator + other_rational_number.numerator}/{self.denominator + other_rational_number.denominator}"

    def subtract_rational_number(self, other):
        if not isinstance(other, RationalNumber):
            return f"{other} is not a fraction"
        return f"{self.numerator - other.numerator}/{self.denominator - other.denominator}"
    
    def multiply_rational_number(self, other):
        if not isinstance(other, RationalNumber):
            return f"{other} is not a fraction"
        return f"{self.numerator * other.numerator}/{self.denominator * other.denominator}"

    def divide_rational_number(self, other):
        if not isinstance(other, RationalNumber):
            return f"{other} is not a fraction"
        return f"{self.numerator * other.denominator}/{self.denominator * other.numerator}"

    def get_float(self):
        return self.numerator / self.denominator


num = RationalNumber(2,4)
num2 = RationalNumber(3,5)

print(num.add_rational_number(num2))
print(num.multiply_rational_number(num2))

print(num)