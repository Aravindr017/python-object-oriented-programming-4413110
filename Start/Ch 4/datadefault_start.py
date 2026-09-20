# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return round(random.uniform(10.0, 100.0), 2)

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = 'No Title'
    author: str = 'No Author'
    pages: int = 0
    price: float  = field(default_factory=price_func)
    
# b1 = Book()
# print(b1)

b2 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
print(b2)
b3 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
print(b3)