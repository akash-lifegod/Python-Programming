n=int(input("Enter no. of rows "))
r=n//2
for i in range(1,r+1):
    for j in range(r-i+1):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i-1):
        print("*",end='')
    print()
print('*'*(r*2)+'*')
for i in range(1,r+1):
    for j in range(i):
        print(" ",end='')
    for j in range(r-i+1):
        print("*",end='')
    for j in range(r-i):
        print("*",end='')
    print()