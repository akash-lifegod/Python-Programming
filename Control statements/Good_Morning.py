# Create a python program capable of greeting you with Good Morning, Good Afternoon 
# and Good Evening. Your program should use time module to get the current hour.


import time
timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
timestamp1 = int(time.strftime('%H'))
# print(timestamp1)
timestamp2 = int(time.strftime('%M'))
# print(timestamp2)
timestamp3 = int(time.strftime('%S'))
# print(timestamp3)
if timestamp1>=0 and timestamp1<=11 and timestamp2<=59:
    print("Good Morning")
elif timestamp1>=12 and timestamp1<=15 and timestamp2<=59:
    print("Good Afternoon")
else:
    print("Good Evening")