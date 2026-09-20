# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    
    
    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    def get_book_list():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist
    
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"booktype must be one of {Book.BOOK_TYPES}")


# TODO: access the class attribute
print('Book types:', Book.get_book_types())

# TODO: Create some book instances
b1 = Book("War and Peace", "HARDCOVER")
# b2 = Book("The Catcher in the Rye", "COMIC")
b3 = Book("The Grapes of Wrath", "PAPERBACK")

# TODO: Use the static method to access a singleton object
thebooklist = Book.get_book_list()
thebooklist.append(b1)
thebooklist.append(b3)

print('Book list:', thebooklist)