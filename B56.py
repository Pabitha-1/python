a=input()
b=0
c=0
for i in a:
    if i>='0' and i<='9':
        c+=1
    if i>='a' and i<='z':
        b+=1
    if i>='A' and i<='Z':
        b+=1
if c>0:
    print('yes')
elif b>0:
    print('no')
