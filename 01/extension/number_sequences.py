x = int(input("Enter the number of beginning: "))
y = int(input("Enter the number of end: "))
print("The even numbers from ",x,"to ", y, ": ")
for i in range(x, y+1):
    if i % 2 == 0:
        print(i, end=' ')
print('\n')
print("The odd numbers from ", x,"to ", y, ": ")
for j in range(x, y+1):
    if j % 2 == 1:
        print(j, end=' ')
print('\n')
print("The squares from ", x,"to ", y, ": ")
for z in range(x, y+1):
    print(z*z, end=' ')
print('\n')
print("That's all.")