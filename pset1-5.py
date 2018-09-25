p=str(input("N:"));
q=len(p)
a=0;
I=1;
V=5;
X=10;
for i in range (q):
    if (p[i]=='I'):
        a=a+1;
    elif (p[i]=='V'):
        a=a+5;
    else:
        a=a+10;
    print (a)

