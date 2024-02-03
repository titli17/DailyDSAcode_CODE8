def merge_sort(arr):
    if (len(arr)>1):
        mid=len(arr)//2      
        l=arr[:mid]
        r=arr[mid:]
        merge_sort(l)
        merge_sort(r)
 
        i=0
        j=0
        k=0
        
        while ((i<len(l))and(j<len(r))):
            if (l[i]<=r[j]):
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
 
        while (i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
 
        while (j<len(r)):
            arr[k]=r[j]
            j+=1
            k+=1
    return arr

def anagram(str1,str2):
    if(len(str1)!=len(str2)):
        return 1
    else:
        l1=list(str1)
        l2=list(str2)
        l1=merge_sort(l1)
        l2=merge_sort(l2)
        flag=0
        for i in range(0,len(l1)):
            if(l1[i]!=l2[i]):
                flag=1
                break
            else:
                flag=0
        return flag

str1=input("Enter first string :")
str2=input("Enter second string :")

a=anagram(str1,str2)
if(a==0):
    print("TRUE\nThe 2 strings are anagrams.")
else:
    print("FALSE\nThe 2 strings are not anagrams.")
