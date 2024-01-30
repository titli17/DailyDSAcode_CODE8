def profit(arr,n):
    max=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                a=arr[j]-arr[i]
                if(a>max):
                    max=a
    return max

n=int(input("Enter the number of elements: "))
arr=[]
print("Enter the elements:")
for i in range(n):
    a=int(input())
    arr.append(a)
print("Stock Prices :",arr)

p=profit(arr,n)
print("Profit =",p)
        
