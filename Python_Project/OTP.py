import random
n=random.random()
print(n)
d=int(input("Enter no. of digits of OTP "))
OTP = str(n)[-d: ]
print(OTP)