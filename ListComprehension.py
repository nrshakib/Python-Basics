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