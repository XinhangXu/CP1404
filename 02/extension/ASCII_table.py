re_times = int(input('How many times you would like to enter: '))
for i in range(re_times):
    # char to ascii
    in_char = input('Enter a character: ')
    #to_asc = in_char.ord()
    print('The ASCII code for {} is {}'.format(in_char,ord(in_char)))

    # ascii to char
    in_number = int(input('Enter a number between 33 and 127: '))
    if in_number >= 33 & in_number <= 127:
        print('The character for {} is {}'.format(in_number, chr(in_number)))
    else:
        print('Not valid number!')
        number = input('Enter a number between 33 and 127: ')
    print('---------')
print('---Finish---')
