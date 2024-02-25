n=int(input("Enter a number :"))
flag=1
if (n==1):
    flag=0
else:
    while(n>1):
        if(n%2==0):
            flag=0
        else:
            flag=1
            break
        n=n/2

if(flag==0):
    print("True.\nIt is a power of 2.")
else:
    print("False.\nIt is not a power of 2.")
