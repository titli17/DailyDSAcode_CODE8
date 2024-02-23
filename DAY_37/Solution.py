s1=input("Enter the string :")
maxi=0
for i in range(0,len(s1)-1):
    count=1
    for j in range(i+1,len(s1)):
        if(s1[i]!=s1[j]):
            count+=1
        else:
            maxi=max(maxi,count)
            break
print("Length of the longest substring without any repeating characters :",maxi)
