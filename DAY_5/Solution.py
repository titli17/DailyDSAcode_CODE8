def remove_duplicates(l,n):
    l1=[]
    l1.append(l[0])
    for i in range(0,n-1):
        j=i+1
        if(l[i]!=l[j]):
            l1.append(l[j])
    return l1    
                
l=[]
n=int(input("Enter the number of elements :"))
print("Enter the elements sorted in non-decreasing order :")
for i in range(0,n):
    a=int(input())
    l.append(a)
print("Array :",l)
l=remove_duplicates(l,n)
print("Final Array :",l)
