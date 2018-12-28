N = input("")
s = sum(e.isspace() for e in N)
w = sum(e.isalpha() for e in N)
d = sum(e.isdigit() for e in N)
sc= len(N)-w-s-d
print(sc)

