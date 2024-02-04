def arrange(arr,n):
    arr1=[]
    count=0
    for i in range(0,n):
        if(arr[i]==0):
            count+=1
        else:
            arr1.append(arr[i])
    for i in range(0,count):
        arr1.append(0)
    print("New Array :",arr1)
    
n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements:")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)

arrange(arr,n)
