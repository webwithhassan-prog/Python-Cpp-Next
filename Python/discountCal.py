import discountLib

price = int(input("Enter Product Price : "))

if price >= 10000 and price < 15000:
    discountLib.discount10(price)
elif price >= 15000 and price < 20000:
    discountLib.discount20(price)
elif price >= 20000 :
    discountLib.discount30(price)
else:
    print("No discount available on this price")