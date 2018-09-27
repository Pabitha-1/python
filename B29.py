m = int(input("N="))
a=0
b=0
for x in range(1,26-1):
    for y in range(1,62-1):
        b=b+1
        if (m == b):
            print(a, ":", y)
            break
    a=a+1

