r=int(input("Enter no. of rows "))
for i in range(1,r+1):
    for j in range(r-i+1):
        print("*",end='')
    print()