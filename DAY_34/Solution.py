n=int(input("Enter the number of lines :"))
for i in range(1,n+1):
    k=i*2-1
    j=0
    s=0
    while(s<n-i):
        print(" ",end="")
        s+=1
    while(j<k):
        print("*",end="")
        j+=1
    print("\n")

for i in range(n,0,-1):
    k=i*2-1
    j=0
    s=0
    while(s<n-i):
        print(" ",end="")
        s+=1
    while(j<k):
        print("*",end="")
        j+=1
    print("\n")
