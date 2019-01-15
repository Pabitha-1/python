p=int(input())
q=int(input())
for i in range(1,(p*q)+1):
    if(i%p==0 and i%q==0):
      print(i)
      break
