purchaseAmount = int(input("enter the purchase amount: "))
couponCode = input("Enter coupon: ").upper()

validCoupon = "SAVE10"
discountOn500 = 0
couponDiscount = 0

if purchaseAmount > 500:
    discountOn500 = purchaseAmount * 0.05

if couponCode == validCoupon:
    couponDiscount = 50

finalAmount = purchaseAmount - discountOn500 - couponDiscount

print(f"""
--------Bill Breakout--------
purchase Amount     : {purchaseAmount}
discount On 500     : {discountOn500}
coupon Discount     : {couponDiscount}
----------------------------
final Amount        : {finalAmount}
""")