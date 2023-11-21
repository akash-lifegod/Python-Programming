ls=[21,23,34]
out=[]
for i in ls:
    a=i-2
out=list(map(lambda a:a*1.8+32,ls))
print(out)