def input1(i):
    l=[]
    print("Enter the number of elements for array",i,":")
    n=int(input())
    print("Enter the elements in sorted manner :")
    for i in range(0,n):
        a=int(input())
        l.append(a)
    return l

l1=input1(1)
l2=input1(2)
print("\n1st Array :",l1)
print("2nd Array :",l2)

l3=list(set(l1)|set(l2))
print("\nUnion :",l3)
