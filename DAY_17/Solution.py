def sort(arr,j,n):
    for i in range(j+1,n-1):
        for k in range(i+1,n):
            if(arr[i]>arr[k]):
                a=arr[i]
                arr[i]=arr[k]
                arr[k]=a

def lexicography(arr,n):
    arr1=[]
    for i in range(0,n):
        arr1.append(arr[i])
    flag=1
    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            if(arr[i]>arr[j]):
                a=arr[i]
                arr[i]=arr[j]
                arr[j]=a
                flag=0
                break
        if(flag==0):
            sort(arr,j,n)
            break
    flag1=0

    if(arr1==arr):
        sort(arr1,-1,n)
        print("Lexicographically next greater permutation not available.\nNew Array :",arr1)
    else:
        print("Lexicographically next greater permutation :",arr)
    

n=int(input("Enter the number of elements :"))
print("Enter the elements :")
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)

lexicography(arr,n)
