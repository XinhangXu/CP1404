items = int(input("Number of items: "))
if items <= 0:
    print(" Invalid number of items! ")
else:
    list = []
    for i in range(0, items, 1):
        x = float(input("Price of item: "))
        list.append(x)
    sumPrice = 0
    for j in range(items):
        sumPrice = sumPrice + list[j]
    if sumPrice > 100:
        sumPrice = round(sumPrice*0.9,2)
        print("Total price for ", items, "items is $", sumPrice)
    else:
        sumPrice = round(sumPrice,2)
        print("Total price for ", items, "items is $", sumPrice)