a=int(input())
for i in range(1,a+1):
  if (a%i)==0:
    if(i<a):
      print(i,end=" ")
    else:
      print(i,end="")
