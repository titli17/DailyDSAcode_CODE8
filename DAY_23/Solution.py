def power(x,n):
    ans=1
    for i in range(1,n+1):
        ans*=x
    return ans

x=float(input("Enter a number :"))
n=int(input("Enter an integer :"))

p=power(x,n)

print("x raised to power n =",p)
