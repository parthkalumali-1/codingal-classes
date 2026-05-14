units = int(input("Enter No. of Units consumed:"))

bill = 0 

if units < 50:
    bill = (units * 2.60) + 25

elif units < 100:
    bill = (50 * 2.60 ) + ((units - 50) * 3.25) + 35

elif units < 200:
    bill = (50 * 2.60) + (50 * 3.25) + ((units - 100) * 5.26) + 45

else:
    bill = (50 * 2.60) + (50 * 3.25) + (100 * 5.26) + ((units - 200 ) * 8.45) + 75

print("Total electricity bill =", bill)
