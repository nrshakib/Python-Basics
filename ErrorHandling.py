# just like try-catch in JavaScript

# try -> try [checks for logic or code to be executed]
# except -> catch [handles if there is any error]
# else -> else [runs if there is no error]
# finally -> finally [runs always despite error or no error]

try:
    a = int(input('Enter a number:'))
    result = 10 / a
    print('Result', result)

except ValueError:
    print('Please enter a valid number')
except ZeroDivisionError:
    print("Can't divide by zero")

else:
    print('There is no error')
    print('The result is', result)

