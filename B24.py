p=[]
q=int(input("Enter the Number:"))
if(1<=q<=1000):
    print("Enter your ",q,"integers")
    for i in range(1,q+1):
        a=int(input(""))
        p.append(a)
    print(p)
    for i in range(len(p)):
        for j in range(i,len(p)):
             if(p[i]>p[j]):
                p[i],p[j]=p[j],p[i]
    print("Order of Number:",p)
else:
    print("invalid input")
