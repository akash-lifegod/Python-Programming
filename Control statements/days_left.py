# Design a program in python to display the number of days left in the current year (2019), when 
# today’s date is entered by the user in format of your choice

day=int(input('Enter day '))
month=int(input('Enter Month '))
days=0
for month in range(1,month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        d=31
    elif month==4 or month==6 or month==9 or month==11:
        d=30
    else:
        d=28
    days=days+d
    #print(days)
for i in range(1,day+1):
    days=days+1
print("Days Passed =",days)
d_left=365-days
print("Days Left =",d_left)
