def search(arr,n,num):
    for i in range(0,n):
        if(arr[i]==num):
            p=i
            break
        else:
            p=-1
    return p

arr=[]
n=int(input("Enter the number of elements :"))
print("Enter the elements :")
for i in range(0,n):
    a=int(input())
    arr.append(a)
print("Array :",arr)
num=int(input("Enter the element you want to search :"))
index=search(arr,n,num)
print("Output :",index)
