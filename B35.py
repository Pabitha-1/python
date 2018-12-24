N = input("")
s  = sum(e.isspace() for e in N)
w   = sum(e.isalpha() for e in N)
o  = len(N) - w - s
print(o)
