# In Python, a function is defined using the def keyword, followed by a function name and parentheses:

# flow
# define a function -> call the function

def my_function():
    print("Hello")

my_function()

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("User") # "User" is an argument

# default parameters

def my_function(country = "Bangladesh"): # Bangladesh is default parameter value here
  print("I am from", country)

my_function("Pakistan")
my_function("Turkiye")
my_function() # counts the default parameter value
my_function("Iran")


# function to find max value

def myFunction(*numbers):
   max_value = numbers[0]
   for num in numbers:
    if num > max_value:
      max_value = num
    return max_value

result = myFunction(10,16,3,7,9)
print(f'{result} is the max value')


# lambda function

# syntax: f = lambda a: a * 2
# [
#   here, f = variable which stores the function
#         lambda = keyword to indicate it's a lambda function
#         a = argument
#         a * 2 = one line expression or logic
# ]

add = lambda a, b: a + b
print(add(3,4))

# mapping
# With map(), you apply a function to every item of the data.

# syntax: map(function, iterable) [ it takes a function and data to map on it]

# convensional function: 
def square(x):
  return x ** 2

numbers = [2,4,5,7]

squares = map(square, numbers) #[a function and iterable data as argument]
print(list(squares))

# lambda function:
numbers = [2,5,6,8]

squares = map(lambda x: x ** 2, numbers) #[a function and iterable data as argument]
print(list(squares))



# filtering
# keep only the items i want accrording to the logic or expression

# syntax: filter(function, iterable) [ it takes a function and data to map on it] [same as map]

numbers = [1, 2, 3, 4, 5]

# convensional function
def evenNumbers(x):
  return x % 2 == 0

even = filter(evenNumbers, numbers)
print(list(even))

# lambda function
odd = filter(lambda x: x % 2 != 0, numbers)
print(list(odd))


# Recursion
# Recursion is when a function calls itself.

# def recursive_function(problem):

#     if base_case:
#         return result

#     # do something

#     return recursive_function(smaller_problem)

def countdown(n):
  if n == 0:
    return # Base Case

  print(n)
  countdown(n - 1) # Recursive Case

countdown(5)

# Two important things: Base Case & Recursive Case

# Recursive function
#        │
#        ├── Base case
#        │      ↓
#        │    STOP
#        │
#        └── Recursive case
#               ↓
#         call itself again


# Factorial of 5
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


# Fibonacci Series
def fibonacci(n):
   if n <= 1:
      return n

   else:
      return fibonacci(n-1) + (n-2)

print(fibonacci(6))


# Generator Function
# A generator is a function that remembers where it stopped and produces its next value whenever you ask for it.
# Generators are functions that can pause and resume their execution.
# The yield keyword is what makes a function a generator.
# Unlike return, which terminates the function, yield pauses it and can be called multiple times.


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)