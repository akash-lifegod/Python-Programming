n=int(input())
sum=0
while n>0:
    r=n%10
    n=n//10
    for i in range(1,r):
        r=r*i
    sum=sum+r
print(sum)
