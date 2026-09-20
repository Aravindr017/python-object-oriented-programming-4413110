# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: add methods for comparison and equality

# Challenge: use a magic method to make stocks and bonds sortable
# Stocks should sort from low to high on price
# Bonds should sort from low to high on yield

class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
        
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
    def __gt__(self, other):
        return self.price > other.price
    def __le__(self, other):
        return self.price <= other.price
    def __ge__(self, other):
        return self.price >= other.price

class Bond:
    def __init__(self, price, name, years, yield_percent):
        self.price = price
        self.name = name
        self.years = years
        self.yield_percent = yield_percent
        
    def __eq__(self, other):
        return self.yield_percent == other.yield_percent
    def __lt__(self, other):
        return self.yield_percent < other.yield_percent
    def __gt__(self, other):
        return self.yield_percent > other.yield_percent
    def __le__(self, other):
        return self.yield_percent <= other.yield_percent
    def __ge__(self, other):
        return self.yield_percent >= other.yield_percent
# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("-----------")
for bond in bonds:
    print(bond)
