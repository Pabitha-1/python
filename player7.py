a = input("enter a string:\n")
b = list(a)
c=''
for i in range(0,len(a)-1,2):
    t=b[i]
    b[i]=b[i+1]
    b[i+1]=t
    c=c+b[i]+b[i+1]
if(len(b)%2!=0):    
    c=c+b[i+2]    
print(c)    
