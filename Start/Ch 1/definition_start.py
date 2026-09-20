# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
    def __init__(self, title):
      self.title = title
      
    def print_title(self):
      print(self.title)

# TODO: create instances of the class
book1 = Book("Brave New World")
book2 = Book('The Great Gatsby')

# TODO: print the class and property
print(book1)
book1.print_title()
book2.print_title()
