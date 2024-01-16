l1=[]
n=int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
    a=int(input())
    l1.append(a)
print("Array :",l1)
max=l1[0]
for i in range(1,n):
    if(max<l1[i]):
        max=l1[i]
print("The largest element in the array is",max,".")
