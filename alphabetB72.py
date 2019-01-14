n=input()
m="aAeEiIoOuU"
f = [each for each in n if each in m]
if len(f)>1:
    print("yes")
else:
    print("no")
