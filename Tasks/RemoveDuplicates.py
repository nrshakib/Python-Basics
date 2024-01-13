numbers = [1,5,68,71,1,52,68,99,1]
newList = []
for number in numbers:
    if number not in newList:
        newList.append(number)
print(newList)