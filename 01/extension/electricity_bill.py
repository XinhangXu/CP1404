print("Electricity bill estimator ")
cents = float(input("Enter cents per kWh: "))
daily = float(input("Enter daily use in kWh: "))
days = float(input("Enter number of billing days: "))
bill = cents * daily * days * 0.01
bills = round(bill, 2)
print("Estimated bill: $",bills)