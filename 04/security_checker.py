usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name_in = str(input("Please enter your UserName: "))
for names in usernames:
    if name_in == names:
        index = 1
        break
    else:
        index = 0
if index == 1:
    print("Access granted")
else:
    print("Access denied")