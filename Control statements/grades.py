a=input("Name")
b=int(input("Roll no. "))
c=float(input("Attendance "))
if c>=75:
    print("Enter your marks")
    m1=int(input())
    m2=int(input())
    m3=int(input())
    m4=int(input())
    m5=int(input())
    m6=int(input())
    i=((m1+m2+m3+m4+m5+m6)*100)/600
    if i>90 and i<=100:
        print("A+")
    elif i>80 and i<=90:
        print("A")
    elif i>70 and i<=80:
        print("B+")
    elif i>60 and i<=70:
        print("B")
    else:
        print("C")
else:
    print("Detained")
