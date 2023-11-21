# Program to find the number of currency notes of each type (Rs. 2000, Rs. 500 and Rs. 100), 
# when the total number of currency notes counted altogether is minimum and there must be at 
# least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user.

amt=int(input('Enter amount to withdraw '))
temp=amt-100
a=temp//2000
temp=temp%2000
b=temp//500
temp=temp%500
c=temp//100 +1
out=f'''No. of 2000 notes = {a}
No. of 500 notes = {b}
No. of 100 notes = {c}'''
print(out)