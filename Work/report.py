# report.py
#
# Exercise 2.4


import csv
import sys
from pprint import pprint
def portfolio_cost(filename):
    portfolio = []
    total_cost = 0.0
    with open( filename , 'rt' , newline='') as file:
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
            d = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(d)
            total_cost += d["shares"] * d["price"]
        # print(total_cost)
        return portfolio

if len(sys.argv) == 2:
    print(portfolio_cost(sys.argv[1]))
else:
    print(portfolio_cost('Data/portfolio.csv'))

# print(portfolio_cost('portfolio.csv'))


def read_prices(filename):
    with open(filename, 'rt', newline = '') as f:
        rows = csv.reader(f)
        prices = []
        for row in rows:
            try:
                t = (
                    row[0],
                    float(row[1])
                )
                # pprint(t)
                prices.append(t)
            except Exception as error:
                ''' the !r shows the representation of the row as a list, type(error).name shows the exceptions type
                error shows the exception message '''
                print(f'Problem with row {row!r}: {type(error).__name__}: {error}')
                continue
        return prices



def compute_gain(prices, portfolio):
    current_portfolio = portfolio_cost(portfolio)
    current_prices = dict(read_prices(prices)) # Changes the list of tuples to a dict, with first item of the tuple being the key 
    for d in current_portfolio:
        current_price = current_prices.get(d['name'])
        if current_price is not None:
            d['change'] = current_price - d['price']
    # pprint(current_portfolio)
    tuples = [tuple(d.values()) for d in current_portfolio]
    return tuples


def make_report(prices, portfolio):
    data = compute_gain(prices, portfolio)
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)

    print('-' * 10, "-" * 10, "-" * 10, "-" * 10)
    for name, shares, price, change in data:
        print(f"{name:>10s} {shares:>10d} {price:9.2f}$ {change:>10.2f}")








                


