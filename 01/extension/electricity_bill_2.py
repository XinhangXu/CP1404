# TARIFF_11 = 0.244618   TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0 ")
option = int(input("Which tariff? 11 or 31: "))
daily = float(input("Enter daily use in kWh: "))
days = float(input("Enter number of billing days: "))
if option == 11:
    bill = 0.244618 * daily * days
elif option == 31:
    bill = 0.136928 * daily * days
bills = round(bill, 2)
print("Estimated bill: $",bills)