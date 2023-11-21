def Lucky_Name(name):
    c=0
    for i in name:
        if i=='A' or i=='a':
            c+=1
        elif i=='E' or i=='e':
            c+=1
        elif i=='I' or i=='i':
            c+=1
        elif i=='O' or i=='o':
            c+=1
        elif i=='U' or i=='u':
            c+=1

    if c==5:
        print(f'{name} is going on trip')
    else:
        print(f'{name} is NOT going')

n=int(input())                                       #no. of students
key=list(map(int,input().split()))                   #Roll no. input
value=list(map(str,input().split()))                 #Student Name input
D={key:value for (key,value) in zip(key,value)}              

for i in range(n):
    name=value[i]
    Lucky_Name(name)
