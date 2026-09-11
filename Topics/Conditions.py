is_true = False
is_false = False

if (is_true):
    print("It's True")
    print('Be true always')
elif (is_false):
    print('I asked you always to be true')
else:
    print('How can it be neither true or false?')
print("Whatever")

# practice

price = 10000
hasGoodCredit = False

if (hasGoodCredit):
    downPayment = 0.1 * price
else:
    downPayment = 0.2 * price
print(f'Down Payment: ${downPayment}')

# Short Hand If ... Else
# If there's one statement for if and one for else, you can put them on the same line using a conditional expression:

a = 2
b = 330
print("A") if a > b else print("B")

# This is called a conditional expression (sometimes known as a "ternary operator").

#syntax
# variable = value_if_true if condition else value_if_false

# Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("Equal") if a == b else print("B")


# Nested If Statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# if statements cannot be empty,
# but if some reason there's an if statement with no content,
# put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass #[The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.]



# Match Statement

# The match statement is used to perform different actions based on different conditions.
# It's like switch-case of JS

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

# underscore ( _ ) is used as the last case value if a code block is to execute when there are not other matches
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

