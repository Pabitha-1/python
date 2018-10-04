a=input("Enter the character:\n")
if(a.isalpha()==True):
    n=['a','e','i','o','u']
    for i in n:
        if(i==a):    
            print("The character is vowel")
            break
    else:
        print("consonant")
else:
    print("Input is invalid")
