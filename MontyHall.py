from random import randint

doors = int(input("Enter the number of doors: "))
iteration = int(input("Enter the number of iterations"))

currentIter = 0;

firstPick = 0

while currentIter < iteration:
    x = randint(0, doors - 1)
    y = randint(0, doors - 1)

    if(x == y):
        firstPick += 1
    
    currentIter += 1

print(str(firstPick) + " : "+ str(firstPick / iteration * 100) + "%")
print(str(iteration - firstPick)  + " : "+ str(((iteration - firstPick) / iteration) * 100) + "%" )
    
