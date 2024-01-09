weight = int(input('Enter Your Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    convertedWeight = weight * 0.45
    print(f'You are {convertedWeight} kg')
else :
    convertedWeight = weight / 0.45
    print(f'You are {convertedWeight} Lbs')