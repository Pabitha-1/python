n=(input("Enter characters:"))
c=0
for x in range(len(n)):
   c=c+1
ch=n.split()
cs=len(ch)
cn=c-(cs-1)
print("character count:",cn)
