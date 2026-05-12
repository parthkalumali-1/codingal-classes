datausage = int(input("Enter data usage:"))
isPrimeUser = input("Are you a prime user (yes/no)")

baseprice = 300
extracharge = 0
discount = 0

if datausage > 5:
    extracharge = 50

priceAfterCharge = baseprice + extracharge

if isPrimeUser == "yes":
    discount = priceAfterCharge * 10/100

finalAmount = priceAfterCharge - discount

print(f"""
-------Recharge Bill-------
Base Price      : {baseprice}
Extra Charge    : {extracharge} 
Prime Discount  : {discount}
----------------------------
Final Amount    : {finalAmount}    
      
     """ )