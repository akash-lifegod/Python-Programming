num=int(input("Enter Number "))
count=0
for i in range(2,num):
    if num%i!=0:
        count=count+1
if count==num-2:
    print("Prime Number")
else:
    print("Not Prime Number")