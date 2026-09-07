# while loop

# syntax: 
        # variable ->
        # while keyword with condition containing variable ->
        # block of code to be executed
        # increment or decrement

i = 1
while i < 3:
  print(i)
  i += 1

# break statement
# using break, the loop stops if the while condition is true

i = 1
while i < 4:
  print(i)
  if i == 2:
    break  # the loop breaks, when i == 2.
  i += 1


# continue statement
# the continue statement stops the current iteration, skips itm abd continues with the next

i = 0
while i < 4:
  i += 1
  if i == 3:
    continue # after 2, when i == 3, it skips the iteration and continues with 4
  print(i)



# For Loop
# syntax: 
        # variable ->
        # for keyword placeholder variable in variable ->
        # block of code to be executed

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# for in string
for x in "banana":
  print(x)

# break statement
# With the break statement the loop can be stopped before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana": # breaks when x == banana
    break



# continue Statement
# With the continue statement the current iteration of the loop can be stopped and skipped
# and continue with the next:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": # skips banana
    continue
  print(x)