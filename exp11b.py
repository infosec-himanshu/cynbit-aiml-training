try:
    f=open("this.txt","r")

    print(f.read())
    f.close()
except FileNotFoundError:
    print("error file not found")
except IOError:
    print("unable to read text")