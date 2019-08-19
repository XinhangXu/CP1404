numbers = []
for i in range(5):
    num = int(input("Number: "))
    numbers.append(num)
print("The first number is ",numbers[0])
print("The last number is ",numbers[-1])
min_num = numbers[0]
for j in numbers:
    if j < min_num:
        min_num = j
print("The smallest number is ",min_num)
max_num = numbers[0]
for k in numbers:
    if k > max_num:
        max_num = k
print("The largest number is ",max_num)
sum = 0
for z in numbers:
    sum = sum + z
print("The average of the numbers is ",sum)