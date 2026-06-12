f=open("this.txt","w")
f.write("hello")
f.close()

f=open("this.txt","r")
content=f.read()
print(content)
