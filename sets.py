# A set is a collection which is 
        # unordered, [Sets are unordered, so you cannot be sure in which order the items will appear.]
        # unchangeable, [Set items are unchangeable, but you can add or remove items.]
        # unindexed [Sets are unindexed, so you cannot access items using an index or a key.]
        # does not allow duplicate values.

fruitsSet = {"apple", "banana", "cherry"}

# The primary difference between a dictionary and a set is: 
            # a dictionary stores data as key-value pairs, 
            # a set stores individual, unique elements

# Accessing set items
# set items can't be accessed by referring to an index or a key as sets are unordered, the items have no index.
# looping through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

fruits = {"apple", "banana", "cherry"}

for x in fruits:
  print(x)


# items of a set can't be changed but new items can be added to a set, and existing items can be removed from a set.
devices = {"laptop", "monitor", "smartphone"}
# add item to set
devices.add("mouse")
devices.add("keyboard")

print('devices after adding mouse and keyboard:',devices)

fruits1 = {"apple", "banana", "cherry"}
fruits2 = {"orange", "kiwi", "mango"}

fruits1.update(fruits2) # The update() method will add items from fruits2 into fruits1
print('fruits1 after updating with fruits2:',fruits1)

# The object in the update() method does not have to be a set,
# it can be any iterable object (tuples, lists, dictionaries etc.).
laptops = {"asus", "hp", "dell"} # this is a set
phones = ["pixel", "iphone", "samsung"] # this is a list

laptops.update(phones)
print(laptops) # The update() method will add items from phones (list) into laptops (set)


# remove item from set
devices.remove("monitor") # remove() method will raise an error if the item to remove doesnot exist
print('devices after removing monitor:',devices)

devices.discard("tablet") # discard() method will not raise an error if the item to remove doesnot exist
print('devices after discarding tablet:',devices)


# You can also use the pop() method to remove an item, but this method will remove a random item,
# so you cannot be sure what item that gets removed.
# the return value of the pop() method is the removed item.

fruits = {"apple", "banana", "cherry"}
x = fruits.pop()

print(x) # output: apple (or banana or cherry) randomly
print(fruits) 

# The clear() method empties the set
countries = {"USA", "Canada", "Mexico"}
countries.clear()
print(countries) # output: set()

# The del keyword will delete the set completely:
cities = {"New York", "Los Angeles", "Chicago"}
# del cities
# print(cities) # output: NameError: name 'cities' is not defined


#Join Sets

# Union of two sets is done with the union() method or the | operator.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)  # or set3 = set1 | set2
print('Union of set1 and set2:', set3)

# Join multiple sets using the union() method or the | operator.
set4 = {"x", "y", "z"}
set5 = {"p", "q", "r"}
set6 = {"s", "t", "u"}

set7 = set4.union(set5, set6)  # or set7 = set4 | set5 | set6
print('Union of set 4 ,5 and 6:', set7)

# The | operator only allows to join sets with sets, 
# not with other data types like can be done with the  union() method.

x = {"a", "b", "c"} #set
y = (1, 2, 3) #tuple
z = [4, 5, 6] #list

allUnion = x.union(y, z) # this will work as union() method can take any iterable object

# allUnion = x|y|z      # this will not work as the | operator can only join sets with sets,
                        # not with other data types like tuple or list

print('Union of set, tuple and list:', allUnion)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print('set1 after updating with set2:', set1)

# Both union() and update() will exclude any duplicate items.

# the Intersection of two sets is done with the intersection() method or the & operator.

# The intersection() method will return a new set, that only contains the items that are present in both sets.
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

set3 = set1.intersection(set2)
# or
# set3 = set1 & set2  # this will also work
print('Intersection of set1 and set2:', set3) # [output: {'c'}]

# The & operator only allows to join sets with sets, 
# not with other data types like can be done with the intersection() method.

# The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print('set1 after intersection update with set2:', set1) # output: {'apple'}

# The difference() method will return a new set that will contain only
# the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
# or
# set3 = set1 - set2  # this will also work
print('Difference of set1 and set2:', set3) # output: {'banana', 'cherry'}



# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
#or 
# set3 = set1 ^ set2  # this will also work
print('Symmetric difference of set1 and set2:', set3) # output: {'microsoft', 'banana', 'google', 'cherry'}



# frozenset() method will make the set immutable (unchangeable),
# meaning you cannot add or remove items from it.
# The frozenset() method returns a frozenset object, which is like a set but cannot be changed after creation.
# The frozenset() method is used to create an immutable set.

x = frozenset({"apple", "banana", "cherry"})
print(x) # output: frozenset({'apple', 'banana', 'cherry'})
print(type(x)) # output: <class 'frozenset'>