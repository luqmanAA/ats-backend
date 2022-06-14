number = int(input("Please enter a 5-digit integer: "))
m_number = number
reversed_number = ""
i = 0
checker = len(str(number))
while i < checker:
    reversed_number += str(m_number % 10)
    m_number = m_number // 10
    i = i + 1
if int(reversed_number) == number:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
