import math
def cal(r):
    return math.pi*r**2
r=float(input("enter the radius"))
area=cal(r)
print(f"area:{area:.2f}")
