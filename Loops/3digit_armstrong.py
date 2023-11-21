#Program to find the series of all three digits Armstrong numbers.
for i in range(100,1000):
    sum=0
    num=i
    while num:
        last=num%10
        sum=sum + (last**3)
        num=num//10
    if sum==i:
        print(i)