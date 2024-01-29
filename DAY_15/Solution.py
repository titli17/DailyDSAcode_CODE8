def sorting(arr,n):
    count0=count1=count2=0
    for i in range(n):
        if(arr[i]==0):
            count0+=1
        elif(arr[i]==1):
            count1+=1
        else:
            count2+=1
    arr1=[]
    for i in range(0,count0):
        arr1.append(0)
    for i in range(0,count1):
        arr1.append(1)
    for i in range(0,count2):
        arr1.append(2)
    
    return arr1        

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements :")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Array :",arr)

a=sorting(arr,n)

print("Sorted Array :",a)
