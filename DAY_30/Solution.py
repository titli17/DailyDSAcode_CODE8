def bubblesort(arr,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                a=arr[i]
                arr[i]=arr[j]
                arr[j]=a

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the number of elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
bubblesort(arr,n)
print("Array after sorting :",arr)








