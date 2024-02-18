def partition(arr,low,high):
    pivot = arr[high]
    i=low-1
 
    for j in range(low,high):
        if(arr[j]<=pivot):
            i=i+1
            (arr[i],arr[j])=(arr[j],arr[i])
 
    (arr[i+1],arr[high])=(arr[high],arr[i+1])
 
    return (i+1)
 
def quick_sort(arr,low,high):
    if(low<high):
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

n=int(input("Enter the number of inputs :"))
arr=[]
print("Enter the elements :")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Array :",arr)

quick_sort(arr,0,n-1)
print("After sorting :",arr)
