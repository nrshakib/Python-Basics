'''
    List in Python is almost same as Array in Js, but List can have multiple data of different data types
    where an Array can hold multiple data of single data type.
'''

names = ['MD', 'Nadim', 'Rijvi' ,'Shakib', 'Prodhan']
print(names[3]) # printing value acccording to the index
names[0] = 'Mohammad' # changing value of item according to index
print(names)

## printing multiple values of diffetent data types
## name?, age?, engineer?, 
profile = [ 'Shakib' , 27, True]
print(profile)

## 2-dimentional List are same as 2-D Array in JS
persons = [
    ['Nadim', 19, True],
    ['Rijvi', 9, False],
    ['Shakib', 1996, True]
]
print(persons)
print(persons[2][0])
for row in persons:
    for item in row:
        print(item)

## List Methods

numbers = [1,12,5,12,45,12,12,3,12,99]
## print the index of mentioned item
print(numbers.index(45))
print(12 in numbers)
## print occurences of a List item
print(numbers.count(12))
## List.append() method to add item at the end of the list
numbers.append(20)
## List.insert() method to add item in the List according to the given index
numbers.insert(2,65)
## List.remove() method to remove mentioned item from the List
numbers.remove(3)
## List.pop() method to remove the last item from the List
numbers.pop()
## List.clear() method to remove all the items from the List
numbers.clear()
print(numbers)

newNumbers1 = [ 5,12,48,3,14,96]
newNumbers1.sort()
print(newNumbers1)

newNumbers2 = [ 5,12,48,3,14,96]
newNumbers2.reverse()
print(newNumbers2)

numbers2 = newNumbers1.copy()
print(numbers2)