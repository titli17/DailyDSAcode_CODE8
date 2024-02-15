def selectionsort(arr,n):
    for i in range(0,n-1):
        small=i
        for j in range(i+1,n):
            if(arr[small]>arr[j]):
                small=j
        a=arr[i]
        arr[i]=arr[small]
        arr[small]=a

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the number of elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
selectionsort(arr,n)
print("Array after sorting :",arr)

