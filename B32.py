a=(input("Enter your sentense:"))
if(len(a)<=1000):
   b=a.split()
   c=len(b)
   print("word:",c)
else:
   print("invalid")
