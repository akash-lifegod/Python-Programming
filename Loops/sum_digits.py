num=int(input("Enter Number "))
sum=0
while num:
    last=num%10
    sum=sum+last
    num=num//10
print(sum)