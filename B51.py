x=[]
y=1
z=1
u=int(input())
v=len(str(u))
z=u
while(u>0):
    y=u%10
    u=u//10
    x.append(y)
for i in range(v-1,-1,-1):
    print(x[i],end=' ')
