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
from pprint import pprint
def portfolio_cost(filename):
    portfolio = []
    total_cost = 0.0
    with open('Data/' + filename , 'rt' , newline='') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            '''
            If you create one dictionary before the loop, update it each time,
            and append it repeatedly, 
            every list entry refers to that same dictionary. 
            After the loop, they’ll all show its final values.
            That's why i'm creating here a new dictionary inside the loop
            '''
            t = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(t)
            total_cost += t["shares"] * t["price"]
        pprint(portfolio)
        return total_cost

if len(sys.argv) == 2:
    print(portfolio_cost(sys.argv[1]))
else:
    print(portfolio_cost('portfolio.csv'))

# print(portfolio_cost('portfolio.csv'))


def read_prices(filename):
    with open(filename, 'rt', newline = '') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                d = {
                    'name' : row[0],
                    'price' : row[1]
                }
                pprint(d)
            except Exception as error:
                ''' the !r shows the representation of the row as a list, type(error).name shows the exceptions type
                error shows the exception message '''
                print(f'Problem with row {row!r}: {type(error).__name__}: {error}')
                continue
