#Q1
print('This is Q1: ')
name = input('Please enter your name here: ')
fw = open('name.txt', 'w')
fw.write(name)
fw.close()
fr = open('name.txt', 'r')
print("My name is ", fr.read())
fr.close()

#gap
print('\n')
for i in range(20):
    print('-',end = '')
print('\n')

#Q2
print('This is Q2: ')
sum = 0
f_num_r = open('numbers.txt', 'r')
for line in f_num_r:
    sum = sum + float(line.strip('\n'))
print('The sum of numbers is ', round(sum,2))
f_num_r.close()
