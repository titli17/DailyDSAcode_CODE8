

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements in sorted manner :")
for i in range(n):
    a=int(input())
    arr.append(a)

print("Array :",arr)

x=int(input("Enter the value of x :"))

flag=1
for i in range(n):
    if(arr[i]==x):
        flag=0
        break
    else:
        if(arr[i]>x):
            flag=1
            break

if(flag==0):
    print("Floor value :",arr[i],"\nCeiling value :",arr[i])
else:
    print("Floor value :",arr[i-1],"\nCeiling value :",arr[i])
