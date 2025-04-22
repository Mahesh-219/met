#assignment - 5

purchase_amount= (float(input("enter the purchase amount: ")))
is_member = (input("are you member?(yes/no): "))
coupon_code = input("enter the coupon code:")

discount = 0
if is_member == "yes":
    if purchase_amount > 100:
        discount = 0.20
    else:
        discount = 0.10
    if coupon_code == "special":
        discount = +0.5
else:
    if purchase_amount > 200:
        discount = 0.10
    elif coupon_code == "special":
        discount = 0.5
final_price = purchase_amount - purchase_amount * discount/100
print(final_price)
