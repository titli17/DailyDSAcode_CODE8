def Recurinsertionsort(arr,n):
    if(n<=1):
        return None
    Recurinsertionsort(arr,n-1)
    a=arr[n-1]
    j=n-2
    while(j>=0 and a<=arr[j]):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=a

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the number of elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
Recurinsertionsort(arr,n)
print("Array after sorting :",arr)
