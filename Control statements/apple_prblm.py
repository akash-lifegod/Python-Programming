# A man has certain number of apples. 
# If he picks them in a group of 7, he can pick all of them. 
# If he picks them in a group of 6, 1 apple is left behind. 
# If he picks them in a group of 5, 1 apple is left behind. 
# If he picks them in a group of 4, 1 apple is left behind. 
# If he picks them in a group of 3, 1 apple is left behind. 
# If he picks them in a group of 2, 1 apple is left behind. 
# Write a program that identifies the minimum number of apples he has

n=1000
for i in range(1,n):
    if i%4==1 and i%5==1 and i%6==1 and i%7==0:
        apple=i
        break
print(apple)