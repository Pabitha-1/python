a1 = int(input(""))
i = 0
n = 0
m = 1
while(i < a1):
    if(i <= 1):
        k = i
    else:
        k = n + m
        n = m
        m = k
    print(k)
    i = i + 1
