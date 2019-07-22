name = str(input("Enter name: "))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = str(input("Enter your choice>>> "))
while choice != 'Q':
   if choice == 'H':
       print("hello",name)
   elif choice == 'G':
       print("goodbye",name)
   else:
       print("invalid message")
   print("(H)ello")
   print("(G)oodbye")
   print("(Q)uit")
   choice = input("Enter your choice>>> ")
print("Finished")