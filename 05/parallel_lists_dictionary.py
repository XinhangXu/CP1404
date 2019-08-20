names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
mydic = {}
for i in range(len(names)):
    key = names[i]
    val = str(dates_of_birth[i])
    val_x = val.strip("()")
    val_y = val_x.replace(',','/',2)
    mydic[key] = val_y
print(mydic)