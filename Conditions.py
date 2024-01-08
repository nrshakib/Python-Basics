is_true = False
is_false = False

if (is_true):
    print("It's True")
    print('Be true always')
elif (is_false):
    print('I asked you always to be true')
else:
    print('How can it be neither true or false?')
print("Whatever")

# practice

price = 10000
hasGoodCredit = False

if (hasGoodCredit):
    downPayment = 0.1 * price
else:
    downPayment = 0.2 * price
print(f'Down Payment: ${downPayment}')