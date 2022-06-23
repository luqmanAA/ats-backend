import csv

# with open(r'week-3\sample.csv', 'r') as f:
#     handler = csv.reader(f)
#     print(len(handler))
#     # for row in handler:
#     #     print(row)

# with open(r'week-3\sample.csv', 'w') as f:
#     handler = csv.writer(f)
#     handler.writerow(['firstname', 'lastname', 'username', 'email', 'phone', 'password'])
#     handler.writerows([['Lukman','Abisoye','luq','labiosye@afexnigeria.com','08160031908',12345],['Awwal','Adeleke','aww','aadeleke@afexnigeria.com','08012345678',67890]])

# with open(r'week-3\sample.csv', 'r') as f:
#     handler = csv.DictReader(f)
#     # print(list(handler))
#     for row in handler:
#         print(row['firstname'])

with open(r'week-3\sample.csv', 'w') as f:
    headers = ["lastname", "firstname", "username", "email", "phone", "password"]
    handler = csv.DictWriter(f, fieldnames=headers)
    handler.writeheader()
    handler.writerows([{'firstname': 'Lukman', 'lastname': 'Abisoye', 'username': 'luq', 'email': 'labiosye@afexnigeria.com', 'phone': '08160031908', 'password': '12345'},{'firstname': 'Lukman', 'lastname': 'Abisoye', 'username': 'luq', 'email': 'labiosye@afexnigeria.com', 'phone': '08160031908', 'password': '12345'}])