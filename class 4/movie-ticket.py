age = int(input("Enter age: "))
student = input("Are you a student (yes/no): ").lower()

basePrice = 200
ageDiscount = 0
studentDiscount = 0

if age < 12:
    ageDiscount = basePrice * 0.5

priceAfterAge = basePrice - ageDiscount

if student == "yes":
    studentDiscount = priceAfterAge * 0.2

finalAmount = priceAfterAge - studentDiscount

print(f"""
--------Ticket Bill--------
Base Price        : {basePrice}
Age Discount      : {ageDiscount}
Student Discount  : {studentDiscount}
--------------------------
Final Amount      : {finalAmount}
""")