number = int(input("Please enter a binary integer: "))
m_number = number
reversed_number = ""
binary_bits = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
converted_bit = 0
i = 0
checker = len(str(number))
while i < checker:
    reversed_number = str(m_number % 10)
    m_number = m_number // 10
    converted_bit += int(reversed_number) * binary_bits[i]
    i = i + 1
    
print(f'The decimal equivalent of {number} is {converted_bit}')