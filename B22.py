  p=[]
q=int(input("N="))
if(1<=q<=100000):
    print("Enter the value ",q,"Integers")
    for x in range(1,q+1):
        a=int(input(""))
        p.append(a)
    print(p)
    m=p[-1]
    s=p[-1]
    for x in p:
        if(m<x):
            m=x
    print("max:",m)
else:
    print("invalid")
