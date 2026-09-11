'''
Regular Way
'''
cities = ['dhaka', 'karachi', 'barcelona','manchester','milan']
newList = []

for x in cities:
    if 'k' in x:
        newList.append(x)

print(newList)

'''
List Comprehension Way
'''
countries = ['bangladesh','pakistan','spain','england','italy']
countryList = [x for x in countries if 'l' in x]
print(countryList)

# Syntax
# newList = [expression for item in iterable if condition == True]

fruits = ['apple','banana','mango','cherry']
upperFriuts = [x.upper() for x in fruits]
print(upperFriuts)


# List comprehension is a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The expressions can be anything, meaning you can put in all kinds of objects in lists.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruits = [fruit for fruit in fruits if "a" in fruit] # new_list = [expression for each item in iterable list]

print(new_fruits)  # Output: ['apple', 'banana', 'mango']


# new_fruits = [ fruit ->  for fruit in fruits -> if "a" in fruit ]
                 # [1]          # [2]                 # [3]

# [1] fruit (The Output): If the check in step 3 is True, the word is saved and added to your new list. 
# If it is False, the word is ignored.
# [2] for fruit in fruits (The Loop): Python loops through your original fruits list one by one.
# In each turn, the current word is assigned to the variable fruit.
# [3] if "a" in fruit (The Filter): Python checks if the letter "a" exists inside that specific word.