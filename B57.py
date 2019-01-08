n=[]
N=int(input())
K=int(input())
for i in range(0,N):
    k=int(input())
    n.append(k)
print(n.count(K))
if(n.count(K)==0):
    print("")
