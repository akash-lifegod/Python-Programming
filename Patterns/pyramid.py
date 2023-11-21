r=int(input("Enter no. of rows "))
for i in range(1,r+1):
    for j in range(r-i):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    for j in range(i-1):
        print("*",end='')
    print()