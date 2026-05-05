num = int(input("Enter Number:"))

if num % 10 == 0 and (num % 11 == 0 or num % 5 == 0):
    print("Number is Divisible by 10 and (11 or 5)")
else:
    print("Not Divisible in this situation")
