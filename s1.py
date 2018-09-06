N=int(input("Num="))
if(N<1000):
  a=N
  cha=0
  while N>0:
    ch=N%10
    cha=cha*10+ch
    N=N/10
    if(t==cha):
      print("It is palindrome")
     else:
      print("It is not palindrome")
