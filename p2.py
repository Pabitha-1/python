a=input("Enter the value:\n")
if(a.isalpha()==False):
    n=int(a)
    if(n<0):
        print("Invalid")
    else:
        if(n%2==0):
            print("even")
        else:
            print("odd")
else:
    print("Input is invalid")
