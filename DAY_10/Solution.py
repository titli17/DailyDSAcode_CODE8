def missing_number(arr,n):
    p=0
    for i in range(0,n-1):
        if(arr[i]!=i+1):
            p=1
            print("Missing number :",i+1)
            break
    if p==0:
        print("Missing number :",i+2)

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter teh elements :")
for i in range(0,n-1):
    a=int(input())
    arr.append(a)
print("Array :",arr)
missing_number(arr,n)

