r=int(input("Enter rows"))
for i in range(1,r+1):
    for j in range(1,r+1):
        print('*',end='') if (i==1 or i==r or j==1 or j==r) else print(" ",end='')
    print()