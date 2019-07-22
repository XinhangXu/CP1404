print("This is question A:")
for i in range(0, 101, 10):
    print(i, end=' ')
print('\n')

print("This is question B:")
for i in range(20,0,-1):
    print(i, end=' ')
print('\n')

print("This is question C:")
num = int(input("Please enter an integer of how many stars you want: "))
for i in range(num):
    print("*",end='')
print('\n')

print("This is question D:")
for i in range(1, num+1, 1):
    for y in range(i):
        print("*",end='')
    print('\n')


