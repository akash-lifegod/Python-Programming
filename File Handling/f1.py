# f=open(r'C:\Users\akash\OneDrive\Desktop\Akash.txt','r')
# out=f.read()
# print(out)
# f.close()
# f=open(r'C:\Users\akash\OneDrive\Desktop\Akash.txt','a')
# f.write('\nOMG I am a Superhero\nNow I feel like saving World !!')
# f.close()
with open(r'C:\Users\akash\OneDrive\Desktop\Akash.txt','r') as f:
    while True:
        line=f.readline()
        print(line,end='')
        if not line:
            break