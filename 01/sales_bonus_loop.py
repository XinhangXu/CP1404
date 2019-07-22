sales = float(input("Enter sales $"))
if sales >= 0:
    while sales > 0:
        if sales < 1000:
            bonus = sales * 0.1
        elif sales >= 1000:
            bonus = sales * 0.15
        print("Bonus is ", bonus)
        sales = float(input("Enter sales $"))
else:
    print("!!!ERROR!!!")