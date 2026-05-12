units = int(input("Enter units consumed: "))

bill = 0
surcharge = 0

if units <= 100:
    bill = units * 5

if units > 100 and units <= 300:
    bill = (100 * 5) + (units - 100) * 7

if units > 300:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

if bill > 1500:
    surcharge = bill * 0.08

finalBill = bill + surcharge

print(f"""
--------Electricity Bill--------
Units Consumed   : {units}
Bill Amount      : {bill}
Surcharge        : {surcharge}
--------------------------------
Final Bill       : {finalBill}
""")