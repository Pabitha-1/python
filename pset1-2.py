a=int(input("N="))
f=1
if (a<0):
   print("invalid")
if (a==0):
   print("The factorial of 0 is 1")
else:
   for i in range(1,a+1):
       f=f*i
   print(f)
