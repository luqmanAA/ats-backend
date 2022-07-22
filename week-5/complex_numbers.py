
class Complex:

    def __init__(self, real_number:float = 1.0, imaginary_number:float = 1.0) -> None:
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def __str__(self) -> str:
        return f"({self.real_number}, {self.imaginary_number})"

    def addComplexNumbers(self, other_complex_number):
        if not isinstance(other_complex_number, Complex):
            return f"{other_complex_number} is not a complex number"
        return f"{self.real_number + other_complex_number.real_number}, {self.imaginary_number + other_complex_number.imaginary_number}i"

    def subtractComplexNumbers(self, other):
        if not isinstance(other, Complex):
            return f"{other} is not a complex number"
        return f"{self.real_number - other.real_number}, {self.imaginary_number - other.imaginary_number}i"



complex_number = Complex(5, 4)
complex_number2 = Complex(3,5)

print(complex_number)
# print(complex_number.addComplexNumbers(complex_number2))
print(complex_number.subtractComplexNumbers(complex_number2))

