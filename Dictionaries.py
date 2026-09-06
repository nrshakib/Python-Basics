# Dictionary is just like object
# It's mutable. Data of a dictionary can be changed
# Dictionary is ordered in python 3.7 and later. In earlier versions like 3.6 and below, it is unordered.

person = {
    'name': 'NRS',
    'age': 40,
    'is_Verified': True
}
print(person)
print(type(person))
print(len(person))

# using get method to get value of a key
print(person.get('home','Panchagarh'))

# change dictionary value
person['name'] = 'Shakib'
print(person['name'])

# update method
car = {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2020
}
car.update({'year': 2021})


# add item to dictionary
car['color'] = 'red'
print('car after adding color:',car)

# items can also be added using update method
car.update({'price': 30000})
print('car after adding price using update method:',car)

# remove items from dictionary

# using pop method [ The pop() method removes the item with the specified key name ]
car.pop('color')
print('car after removing color:',car)

# using del keyword [ The del keyword removes the item with the specified key name ]
del car['price']
print('car after removing price using del keyword:',car)

# The del keyword can also delete the dictionary completely:
# del car
# print('car after deleting the dictionary completely:',car)

# The clear() method empties the dictionary:
# car.clear()
# print('car after clearing the dictionary:',car)


# Loop Through a Dictionary

# this will loop through all the keys of the dictionary, and print them one by one:
for x in car:
  print(x)  # output: brand, model, year

# another method to loop through all the keys is to use the keys() method:
for x in car.keys():
  print(x)  # output: brand, model, year

# this will loop through all the values of the dictionary, and print them one by one:
for x in car:
  print(car[x])  # output: Toyota, Camry, 2021

# another method to return values is to use the values() method:
for x in car.values():
  print(x)  # output: Toyota, Camry, 2021

# Loop through both keys and values, by using the items() method:
for x, y in car.items():
  print(x, y)  # output: brand Toyota, model Camry, year 2021



# nested dictonary [multiple dictionaries inside a dictionary]
devices = {
    'laptop': {
        'brand': 'Asus',
        'model': 'Vivobook 15',
        'year': 2019
    },
    'phone': {
        'brand': 'Realme',
        'model': '7 pro',
        'year': 2021
    }, 
    'monitor': {
        'brand': 'msi',
        'model': 'unknown',
        'year': 2026
    }
}

print('My devices:',devices)

# To access items from a nested dictionary, use the name of the dictionaries, starting with the outer dictionary:
print('My laptop:',devices['laptop'])
print('My phone:',devices['phone'])

# To access items from a nested dictionary, use the keys to navigate through the dictionaries:
print('My monitor brand:',devices['monitor']['brand'])

# to loop through a nested dictionary, use a for loop to iterate through the outer dictionary,
# and then use another for loop to iterate through the inner dictionaries:

for device, specs in devices.items(): 
    # devices is the outer dictionary, device is the key of the outer dictionary,
    # and specs is the inner dictionary
    print(f"{device}:")
    for key, value in specs.items():
        print(f"  {key}: {value}")