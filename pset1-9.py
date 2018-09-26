a=int(input("I="))
b=int(input("r="))
if(a,b<=100000):
    f=0
    c=0
    for m in range(a,b+1):
        f=0
        for n in range(1,m+1):
            if(m%n==0):
                f=f+1
        if(f==2):
             c=c+1
    print(c)
else:
    print("Invalid")
