p=[]
num=int(input())
for i in range(0,num):
  q=int(input())
  p.append(q)
p.sort()
print(p[0],p[num-1])
