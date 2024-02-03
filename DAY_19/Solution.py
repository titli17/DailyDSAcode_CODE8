def pairsum(arr,n,target):
    flag=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==target):
                arr1=[]
                arr1.append(i)
                arr1.append(j)
                print("YES (for 1st variant)")
                print(arr1,"(for 2nd variant)\n")
                flag=1
    if(flag==0):
        print("NO")

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
target=int(input("Enter the target variable :"))

pairsum(arr,n,target)
