n=int(input("Enter the dividend : "))
m=int(input("Enter the divisor : "))

m1=n1=0

if(m<0):
    m1-=m
else:
    m1=m

if(n<0):
    n1-=n
else:
    n1=n
    
count=0
while(n1>=m1):
    count+=1
    n1-=m1

if((m<0 and n<0) or(m>0 and n>0)):
        print("Quotient =",count)
else:
    print("Quotient =",0-count)
