from tabulate import tabulate

last_month_sales = [[50, 25, 40, 70], [69, 40, 25, 85], [105, 25, 45, 60], [55, 35, 73, 39], [20, 60, 55, 20]]

total_by_sales = [sum(elts) for elts in zip(*last_month_sales)]
total_by_products = [sum(i) for i in last_month_sales]

sales = [total_by_sales,total_by_products]

sales[0].insert(0, "Total by sales")

table_list = [
    ['Product 1: ', 50, 25, 40, 70,],
    ['Product 2: ', 69, 40, 25, 85],
    ['Product 3: ', 105, 25, 45, 60],
    ['Product 4: ', 55, 35, 73, 39],
    ['Product 5: ', 20, 60, 55, 20],
    sales[0]
    ]

for i in range(len(sales[1])):
    table_list[i].append(sales[1][i])

# print(sales)

print(tabulate(table_list, headers=["Sales Rep 1", "Sales Rep 2", "Sales Rep 3", "Sales Rep 4", "Total by Products"]))
