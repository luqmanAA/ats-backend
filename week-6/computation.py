
class Computation:

    def __init__(self) -> None:
        pass

    def factorials(self, number):
        'calculates the factorial of <number>.'

        if number == 0 or number == 1:
            return 1
        return number * self.factorials(number - 1)

    def sum(self, number):
        'calculates the sum of the first n (<number>) integers i.e 1 + 2 + 3 + .. + n(<number>)'

        if number == 1:
            return 1
        return number + self.sum(number - 1)

    def prime_check(self, number):
        'tests the primality of <number>'

        if number <= 1:
            return False
        for i in range(2,number):
            if number % i == 0:
                return False
        return True

    def test_prim(self, number):
        'tests the primality of <number>'

        if self.prime_check(number):
            return f"{number} is a prime number"
        return f"{number} is not a prime number"

    def table_mult(self, number):
        'creates and displays the multiplication table of <number>'

        for i in range(1,13):
            print(f"{number} x {i} = {number * i}")  

    def all_table_mult(self):
        'display all the integer multiplication tables 1, 2, 3, ..., 9'

        for i in range(1,10):
            self.table_mult(i)

    @staticmethod
    def list_div(number):
        'gets all the divisors of <number> on new list'

        return [divisor for divisor in range(1,number) if number % divisor == 0 ]
        # return list_of_divisors

    def list_div_prim(self,number):
        'gets all the prime divisors of <number>'
        
        return [n for n in Computation.list_div(number) if self.prime_check(n)]
        # return list_of_prime_divisors


compute = Computation()

# print(compute.factorials(6))
# print(compute.sum(6))
print(compute.test_prim(997))
# compute.all_table_mult()

print(compute.list_div(20))
print(compute.list_div_prim(20))