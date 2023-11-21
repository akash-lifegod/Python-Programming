n=int(input())
l=len(format(n,'b'))
p=n+1
for i in range(p):
    print(' '*(l-len(format(i,'b')))+format(i,'b'))