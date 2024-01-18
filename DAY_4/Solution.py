def selection_sort(l,n):
    for i in range(0,n-1):
        small=i
        for j in range(i+1,n):
            if(l[small]>l[j]):
                small=j
        a=l[i]
        l[i]=l[small]
        l[small]=a

n=int(input("Enter the number of elements : "))
l=[]
print("Enter the elements :")
for i in range(0,n):
    a=int(input())
    l.append(a)
print("Array :",l)
selection_sort(l,n)
print("Sorted Array :",l)
