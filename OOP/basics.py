# OOP = A way of orgnaizing code by creating blueprints


# Advantages of OOP
#  i) Clear code structure
# ii) Easy to maintain and reuse
# iii) Reusable and less code without repeating same code

# A Class is like an object constructor, or a "blueprint" or template for creating objects.

# class keyword is used to create a class

# Object is the instance or in simple words, created item using the class template
class MyClass: # [ This is how class is created]
  student = 5

c1 = MyClass() # [ This is how object is created from the class ]
print(c1.student)

# __init__ method

# __init__() is a special method that runs automatically when you create an object.
# The __init__() method is called automatically every time the class is being used to create a new object.
class Person:
    def __init__(self):
        print("A person object was created")

person1 = Person() # [ Output: A person object was created]

# Without the __init__() method, you would need to set properties manually for each object:
class Person:
  pass

p1 = Person()
p1.name = "Mobias"
p1.age = 55

print(p1.name)
print(p1.age)

# Using __init__() makes it easier to create objects with initial values:
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

p1 = Person("Sylvie", 25)

print(p1.name)
print(p1.age)

# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# self simply means Store this value inside this particular object.
# The self parameter must be the first parameter of any method in the class.

# It does not have to be named self, you can call it whatever you like, 
# but it has to be the first parameter of any method in the class
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def greet(self):
      print("Hello", self.name)

person1 = Person("Loki", 30)
person1.greet() # [ Output: Hello Loki ]

# Class Properties

# Properties are variables that belong to a class. They store data for each object created from the class.

# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects


# Class Methods

# Methods are functions that belong to a class. They define the behavior of objects created from the class.
# All methods must have self as the first parameter.

class Student: 
    roll = ''
    gpa = ''

    def setValue(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f'Roll: {self.roll},GPA:{self.gpa}')


Shakib = Student()
Shakib.setValue(75,3.11)
Shakib.display()

Rijvi = Student()
Rijvi.setValue(10,3.99)
Rijvi.display()