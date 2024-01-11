numbers = [2,21,15,98,55,3]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(f'Maximum number is {max}')