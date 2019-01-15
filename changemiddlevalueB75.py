a=list(input())
if len(a)%2:
	a[len(a)//2]="*"
else:
	a[(len(a)//2)-1]="*"
	a[len(a)//2]="*"
print("".join(a))
