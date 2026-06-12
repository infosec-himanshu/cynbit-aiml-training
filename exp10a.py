data=float(input("enter the data in gb:"))
if data <=2:
    bill=data*50
elif data<=5:
    bill=(2*50)+((data-2)*40)
else:
    bill=((2*50)+(3*40)+(data-5)*30+100)
print(f"total databill{bill}")