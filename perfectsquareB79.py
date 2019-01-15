p=int(input())
q=int(input())
flag=0
r=p*q
for i in range(0,r+1):
    if(i**2==r):
      flag=flag+1
if(flag==1):
    print("yes")
else:
    print("no")
