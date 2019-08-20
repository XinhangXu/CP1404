# TARIFF_11 = 0.244618   TARIFF_31 = 0.136928  TARIFF_21 = 0.196928  TARIFF_41 = 0.276948  TARIFF_51 = 0.206423
ele_dic = {
    "11": "0.244618",
    "21": "0.196928",
    "31": "0.136928",
    "41": "0.276948",
    "51": "0.206423"
}
print("Electricity bill estimator *dic_vison")
option = str(input("Which tariff? 11 / 21 / 31 / 41 / 51 : "))
daily = float(input("Enter daily use in kWh: "))
days = float(input("Enter number of billing days: "))
for key in ele_dic:
    if option == key:
        bill = float(ele_dic[key]) * daily * days
bills = round(bill, 2)
print("Estimated bill: $",bills)