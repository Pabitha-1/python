z=[]
x=1
y=1
u=int(input())
v=len(str(u))
y=u
while(u>0):
    x=u%10
    u=u//10
    z.append(x)
for i in range(v-1,-1,-1):
    print(z[i],end=' ')
