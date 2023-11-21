s=input()
ls=['I','V','X','L','C','D','M']
l=[]
l.extend(s)
out=0
for i in range(len(l)-1):
    if l[i]=='I':
        if l[i+1] not in ['V','X','L','C','D','M']:
            out+=1
        else:
            out=out-1
    elif l[i]=='V':
        if l[i+1] not in ['X','L','C','D','M']:
            out=out+5
        else:
            out=out-5
    elif l[i]=='X':
        if l[i+1] not in ['L','C','D','M']:
            out=out+10
        else:
            out=out-10
    elif l[i]=='L':
        if l[i+1] not in ['C','D','M']:
            out=out+50
        else:
            out=out-50
    elif l[i]=='C':
        if l[i+1] not in ['D','M']:
            out=out+100
        else:
            out=out-100
    elif l[i]=='D':
        if l[i+1] not in ['M']:
            out=out+500
        else:
            out=out-500
    else:
        out=out+1000
if l[len(l)-1]==ls[0]:
    out=out+1
elif l[len(l)-1]==ls[1]:
    out=out+5
elif l[len(l)-1]==ls[2]:
    out=out+10
elif l[len(l)-1]==ls[3]:
    out+=50
elif l[len(l)-1]==ls[4]:
    out+=100
elif l[len(l)-1]==ls[5]:
    out+=500
else:
    out+=1000
print(out)