def printing(mat,r,c):
    print("\nMatrix :")
    for i in range(0,r):
        for j in range(0,c):
            print(mat[i][j],end=" ")
        print("\n")

def rotate(mat1,r,c):
    mat2=[]
    for i in range(0,c):
        a=[]
        for j in range(0,r):
            b=mat1[r-1-j][i]
            a.append(b)
        mat2.append(a)
    return mat2

r=int(input("Enter the number of rows :"))
c=int(input("Enter the number of columns :"))
mat1=[]
print("Enter the elements :")
for i in range(0,r):
    a=[]
    for j in range(0,c):
        b=int(input())
        a.append(b)
    mat1.append(a)
printing(mat1,r,c)
    
mat2=rotate(mat1,r,c)
print("After 90 degrees clockwise rotation :")
printing(mat2,c,r)
