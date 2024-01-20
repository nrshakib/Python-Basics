'''
    Tuple is one of the built-in data types in Python.
    A Python tuple is a sequence of comma separated items, enclosed in parentheses ().
    The items in a Python tuple need not be of same data type.
    We can only get info from a Tuple.We can't change it.
'''

tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)

tup5 =  (tup1[1],) * 4
print(tup5)


'''
    Subtuple from a Tuple
    Subtuple = tup3[i : j]

    Here tup3 is a tuple
    i : index of the first item in the subtup
    j : index of the item next to the last in the subtup
'''
subTuple = tup3[1:3]
print(subTuple)

'''
    To Change or Update Tuple element: 
    i) convert the tuple to a list,
    ii) update an existing item, 
    iii) append a new item and sort the list.
    iv) Convert the list back to tuple.
'''
tup1 = ("a", "b", "c", "d")
print ("Tuple before update", tup1, "id(): ", id(tup1))

# convert Tuple to List
list1 = list(tup1)
# Update item
list1[2]='F'
# Apply list methods on the converted list
list1.append('Z')
list1.sort()
print ("updated list", list1)
# Convert the list back to tuple
tup1 = tuple(list1)
print ("Tuple after update", tup1, "id(): ", id(tup1))

'''
    Unpacking in Python is like Destructuring in Js
'''
tupX = (10, 20, 30, 40, 50, 60)
*x, y, z = tupX
print ("x: ",x, "y: ", y, "z: ", z)