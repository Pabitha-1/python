f = int(input(""))
c = 0
a = 0
b = 1
while(c< f):
    if(c <= 1):
        k = c
    else:
        k = a + b
        a = b
        b = k
    print(k)
    c = c + 1
