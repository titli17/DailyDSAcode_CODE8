def merge_sort(arr):
    if (len(arr)>1):
        mid=len(arr)//2      
        l=arr[:mid]
        r=arr[mid:]
        merge_sort(l)
        merge_sort(r)
 
        i=0
        j=0
        k=0
        
        while ((i<len(l))and(j<len(r))):
            if (l[i]<=r[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
 
        while (i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
 
        while (j<len(r)):
            arr[k]=r[j]
            j+=1
            k+=1
 
n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
merge_sort(arr)
print("Sorted Array :",arr) 
