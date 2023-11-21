n=input()
l=len(n)
ls=list(n)
t=[int(i) for i in ls]
sum=0                                                 #Armstrong Number
for i in range(0,l,1):
    sum=sum+((t[i])**l)
print(sum)
if int(n)==sum:
    print('Armstrong')