# multi line string 

line = '''
Hello,
Welcome to Python.
Happy Learning
'''
print(line)

# string indexes

name = "Jennifer"
print(name)
print(name[2])
print(name[-4])
print(name[1:-1])

# formatted strings

first = 'John'
last = 'Snow'
region = 'North'
# target: John Snow is the king of the [North]

#typical way
option01 = first + ' ' + last + ' ' + 'is the king of the ' + '[' + region +']'
print(option01)

#formatted string
option02 = f'{first} {last} is the king of the [{region}]'
print(option02)

# string methods

file = 'Python Strings'
print(len(file))
print(file.upper())
print(file.lower())
print(file.find('n'))
print(file.find('Strings'))
print(file.replace('Strings', 'String'))
print('Python' in file)