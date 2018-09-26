a=input("Enter the String1:")
b=input("Enter the string2:")
m=0
n=0
if(len(a),len(b)<=100000):
   for m in range(len(a)):
            if(a[m]!=b[m]):
                n=n+1
   if(n==1):
        print("yes")
   else:
        print("no")
else:
    print("invalid")

