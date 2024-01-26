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

def find_single(arr,n):
    c=0
    for i in range(0,n-2):
        if(i==0):
            if(arr[i]!=arr[i+1]):
                return(arr[i])
        else:
            if((arr[i]!=arr[i+1])and(arr[i+1]!=arr[i+2])):
                c=1
                return(arr[i+1])
    if(c==0):
        return(arr[n-1])
    

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
merge_sort(arr)
s=find_single(arr,n)
print("The number that appears only once is",s,".")


