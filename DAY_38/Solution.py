coins=[1000,500,100,50,20,10,5,2,1]

n=int(input("Enter the amount :"))

arr=[]
count=0
i=0
while(n>0):
    if(n>=coins[i]):
        count+=1
        n-=coins[i]
        arr.append(coins[i])
    else:
        i+=1
print("Minimum number of denominations :",count)
j=p=0
while(j<len(arr)-1):
    c=1
    for k in range(j+1,len(arr)):
        if(arr[j]==arr[k]):
            c+=1
        else:
            print(c,"note/coin of",arr[j])
            j=k
            break
    p=c
    if(k==len(arr)-1):
        break

print(p,"note/coin of",arr[j])
