a1= int(input("hour:"))
b1= int(input("minute:"))
a2= int(input("enter your second hour and minute; hour:"))
b2= int(input("minute:"))
a=a1-a2
b=b1-b2
if(b<0):
    ae=a-1
    be=60+b
    print(ae,":",be)
else:
    print(a,":",b)

