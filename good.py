def add(*numbers): #store in a tuple
    total=sum(numbers) 
    print(f"sum of numbers {numbers} is {total}")
def printinfo(**info): #store in a dictionary form
    for key,value in info.items(): # python redirect to (key,tuple)
        print(f"{key}:{value}")
printinfo(name="david",profession="engineer",country="usa")
add(1,2,3,4,5)

