print("Enter '0' for exit.");
pp=input("Enter any character: ");
if pp=='0':
   exit();
else:
   if((pp>='a' and pp<='z') or (pp>='A' and pp<='Z')):
    	print(pp, "is an alphabet.");
   else:
    	print(pp, "is not an alphabet.");
