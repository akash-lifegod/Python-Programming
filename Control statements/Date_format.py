n=int(input())
for i in range(n):
    s=[]
    s.extend(input())
    if int(s[0]+s[1]) > 12 and int(s[3]+s[4])<=12:
        print('DD/MM/YYYY')
    elif int(s[0]+s[1]) <= 12 and int(s[3]+s[4])>12:
        print('MM/DD/YYYY')
    else:
        print('BOTH')