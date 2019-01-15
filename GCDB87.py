p=int(input())
q=int(input())
for i in range(q,0,-1):
    if(p%i==0 and q%i==0):
      print(i)
      break
