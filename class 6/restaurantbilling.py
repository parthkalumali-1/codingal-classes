foodtotal = int(input("Enter food total: "))
servicecharge = int(input("Enter service charge (5 or 10): "))
membership = input("Do you have membership (yes/no): ")

charge = foodtotal * servicecharge / 100

billaftercharge = foodtotal + charge

discount = 0

if membership == "yes":
    discount = billaftercharge * 5 / 100

finalBill = billaftercharge - discount

print(f"""
-------Restaurant Bill-------
Food Total      : {foodtotal}
Service Charge  : {charge}
Membership Disc : {discount}
------------------------------
Final Bill      : {finalBill}
""")