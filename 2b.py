def separate(price):
    rupees=int(price)
    paise=round((price-rupees)*100)
    return rupees,paise
price=float(input("enter the price):"))
rupees,paise =separate(price)
print(f"rupees:{rupees}")
print(f"paise:{paise}")
