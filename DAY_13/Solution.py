def longest(arr,n,k):
    length=0
    for i in range(0,n):
        sum1=0
        for j in range(i,n):
            sum1+=arr[j]
            if(sum1==k):
                if(length<j-i+1):
                    length=j-i+1
    return length
        

n=int(input("Enter the number of elements :"))
print("Enter the elements :")
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
k=int(input("Enter the sum :"))
length=longest(arr,n,k)
print("Length of the longest subarray that sums to",k,"is",length,".")
