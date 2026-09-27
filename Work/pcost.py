# pcost.py
#
# Exercise 1.27

# total = 0
# with open('Data/Portfolio.csv' , 'r') as file:
#     headers = next(file)
#     for line in file:
#         name, share, price = line.split(',')
#         total += float(share)*float(price)

# print(f"The total is {total:.2f}")



# def portfolio_cost(filename):
#     total = 0
#     with open('Data/' + filename , 'r') as file:
#         headers = next(file)
#         for line in file:
#             name, share, price = line.split(',')
#             try:
#                 total += float(share)*float(price)
#             except ValueError:
#                 print('This is a bad value, moving on')
#     # print(f"The total is {total:.2f}")
#     return total

# print(portfolio_cost('portfolio.csv'))
import csv
import sys

def portfolio_cost(filename):
    total = 0
    with open('Data/' + filename , 'r') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            name, share, price = row
            try:
                total += float(share)*float(price) 
            except ValueError:
                print('This is a bad value, moving on')
    # print(f"The total is {total:.2f}")
    return total

if len(sys.argv) == 2:
    print(portfolio_cost(sys.argv[1]))
else:
    print(portfolio_cost('portfolio.csv'))

# print(portfolio_cost('portfolio.csv'))