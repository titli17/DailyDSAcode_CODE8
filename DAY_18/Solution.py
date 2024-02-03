def set_matrix_zero(arr,r,c):
    for i in range(0,r):
        for j in range(0,c):
            if(arr[i][j]==0):
                arr[i][j]='a'
    for i in range(0,r):
        for j in range(0,c):
            if(arr[i][j]=='a'):
                arr[i][j]=0
                for k in range(0,c):
                    if(arr[i][k]=='a'):
                        continue
                    else:
                        arr[i][k]=0
                for l in range(0,r):
                    if(arr[l][j]=='a'):
                        continue
                    else:
                        arr[l][j]=0
    return arr

r=int(input("Enter the number of rows :"))
c=int(input("Enter the number of columns :"))
print("Enter the elements :")
arr=[]
for i in range(0,r):
    arr1=[]
    for j in range(0,c):
        a=int(input())
        arr1.append(a)
    arr.append(arr1)
print("\nMatrix:")
for i in range(0,r):
    for j in range(0,c):
        print(arr[i][j],end="  ")
    print("\n")

arr=set_matrix_zero(arr,r,c)
print("New Matrix:")
for i in range(0,r):
    for j in range(0,c):
        print(arr[i][j],end="  ")
    print("\n")

    
