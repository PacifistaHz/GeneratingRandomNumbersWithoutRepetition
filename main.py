start=input("Enter a start number: ")
end=input("Enter a end number: ")
generatingNumber=input("Enter a generating number: ")
start=int(start)
end=int(end)
generatingNumber=int(generatingNumber)

array=list()

import random
while True:
    number=random.randint(start,end)
    if array.count(number)>0:
        continue
    else:
        array.append(number)
        generatingNumber -= 1
    if generatingNumber == 0:
        break
print(*array, sep="\n")