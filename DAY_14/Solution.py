def maxSubarraySum(arr,n):
    max_so_far=max_ending_here=0
    for i in range(1,n):
        max_ending_here=max(arr[i],max_ending_here+arr[i])
        max_so_far=max(max_so_far,max_ending_here)
    return(max_so_far)

n=int(input("Enter the number of elements :"))
arr=[]
print("Enter the elements :")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Array :",arr)

maxsum=maxSubarraySum(arr,n)
print("Maximum subarray sum in the array is",maxsum,".")
