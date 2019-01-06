p=int(input())
q=0
while(p>0):
    reminder=p%10
    q=q+reminder
    p=p//10
print(q)
