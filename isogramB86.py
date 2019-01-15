p=input()
flag=0
for i in range(0,len(p)):
    if(p.count(p[i])>1):
        flag=flag+1
if(flag==0):
    print("yes")
else:
    print("no")
