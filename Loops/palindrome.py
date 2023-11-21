n=int(input("Enter number "))
k=n
s=0
while n:
    l=n%10
    s=s*10+l
    n=n//10
if s==k:
    print("Palindrome")
else:
    print("Not Palindrome")