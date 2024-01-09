# Logical Operator
# AND, OR, NOT

good_Batter = True
good_Bowler = False

if good_Batter and not good_Bowler:
    print('He is an all rounder')
else:
    print('He is not an all rounder')


# Comparison Operator
    
name = 'Python'

if len(name) < 3:
    print("Name Must Be Of Minimum 3 Characters")
elif len(name) > 10:
    print("Name can be of 10 characters max")
else:
    print("Everything is Okay")