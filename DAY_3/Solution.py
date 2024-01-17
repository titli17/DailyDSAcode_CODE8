l=[]
n=int(input("Enter the number of elements : "))
print("Enter the elements :")
for i in range (0,n):
    a=int(input())
    l.append(a)
print("Array :",l)
flag=0
for i in range(0,n):
    if i!=n-1:
        if(l[i]>l[i+1]):
            print("FALSE!\nIt is not sorted.")
            break
        else:
            flag=1
if flag==1:
    print("TRUE!\nIt is sorted.")
