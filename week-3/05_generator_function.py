from math import factorial


def loop():
    l = [1, 2,3,4]
    for num in l:
        yield num

f = loop()

# for r in f:
#     print(r)
# print(next(f))
# print(next(f))
# d = {'k':'v'}

# print(type(d.keys()))

def read_file(file_name):
    for row in (open(file_name, 'r')):
        if row != '\n':
            yield row

i = read_file(r'week-3/user_accounts.csv')
print(next(i))
print(next(i))
print(next(i))
print(next(i))