def mnum(num):
    print(f"inside before modi.:num={num}")
    num=num+10
    print(f"after modification:num={num}")

nnum=5
print(f"before:mnum={nnum}")

mnum(nnum)
print(f"after:num={nnum.num}")
