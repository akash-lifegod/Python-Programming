a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
if a>b and a>c:
    print("{} is largest".format(a))
elif b>c and b>a:
    print("{} is largest".format(b))
else:
    print("{} is largest".format(c))