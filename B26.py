A=[]
N=int(input("Values="))
if(1<=N<=1000):
  print(N)
  for i in range(1,N+1):
    a=int(input(""))
    A.append(a)
  print(sorted(A))
else:
    print("invalid")
