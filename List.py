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