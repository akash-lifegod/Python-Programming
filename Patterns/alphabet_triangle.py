r=int(input("Enter no. of Rows "))
a=65
for i in range(1,r+1):
    for j in range(i):
        print(chr(a),end='')
        if a<=89:
            a=a+1
        else:
            a=65
    print()