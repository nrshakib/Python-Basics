# Magic methods are special methods whose names start and end with double underscores
# Because of the double underscores, they are also called dunder methods (short for "double underscore").

# e.g: __init__() and __str__()

# The __str__() method controls what is returned when the object is printed, or passed to str().
# __str__() must return a string. If it returns anything else, Python raises a TypeError.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 25)
print(p1)


# __repr__ means representation. ** A technical representation, meant for developers
# __repr__() controls how an object is represented as a string, mainly for developers/debugging.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Shakib", 25)
print(person)