def count(arr,n):
    count=p=0
    for i in range(0,n):
        if(arr[i]==1):
            count+=1
        else:
            if(p<count):
                p=count
            count=0
    if(p>count):
        return p
    else:
        return count

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
num=count(arr,n)
print("Maximum number of consecutive 1's in the array is",num,".")
