a=int(input())
b=str(a)
if((b.count("0")+b.count("1"))==len(str(a))):
    print("yes")
else:
    print("no")
