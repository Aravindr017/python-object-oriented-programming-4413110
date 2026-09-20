# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_method(self):
        self.value1 = "New Value"  # This will raise a dataclasses.FrozenInstanceError

obj = ImmutableClass('Another Value', 42)
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "New Value"  # This will raise a dataclasses.FrozenInstanceError
# print(obj.value1, obj.value2)
# TODO: even functions within the class can't change anything
# obj.some_method()  # This will raise a dataclasses.FrozenInstanceError
