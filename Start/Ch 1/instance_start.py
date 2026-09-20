# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attribute'  # double underscore makes it private

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount     # _ in frnt to set the variable as protected 

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 29.99)
b2 = Book("The Catcher in the Rye", "J.D. Salinger", 278, 19.99)

# TODO: print the price of book1
print(b1.get_price())



# TODO: try setting the discount
print(b2.get_price())
b2.set_discount(0.25)       # 25% discount
print(b2.get_price())

# TODO: properties with double underscores are hidden by the interpreter
print(b1.__secret)  # This will raise an AttributeError