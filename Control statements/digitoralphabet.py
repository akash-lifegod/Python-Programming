'''n=input("Enter here")
out="Alphabet" if n>='A' and n<='Z' or n>='a' and n<='z' else "Digit" if n>='0' and n<='9' else "Special Character"
print(out)'''
n=input("Enter here")
if n>='A' and n<='Z' or n>='a' and n<='z':
    print('Alphabet')
elif n>='0' and n<='9':
    print("Digit")
else:
    print("Special Character")
    
