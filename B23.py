p=[]
q=int(input("N="))
if(1<=q<=100000):
    print("enter your ",q,"integers")
    for x in range(1,q+1):
        a=int(input(""))
        p.append(a)
    print(p)
    r=p[-1]
    s=p[-1]
    for x in p:
        if(r>x):
            r=x
    print("minimum:",r)
else:
    print("invalid")
