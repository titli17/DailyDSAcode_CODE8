#row-wise sorted matrix
#assumption :- r*c is odd

r=int(input("Enter the number of rows :"))
c=int(input("Enter the number of columns :"))
print("Enter the elements :")

arr=[]
list1=[]

for i in range(r):
    arr1=[]
    for j in range(c):
        a=int(input())
        arr1.append(a)
        list1.append(a)
    arr.append(arr1)

print("Matrix :")
for i in range(r):
    for j in range(c):
        print(arr[i][j],end=" ")
    print("\n")

list1=sorted(list1)

index=int(((r*c)-1)/2)

print("Median =",list1[index])
