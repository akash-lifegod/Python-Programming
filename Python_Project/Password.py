import random
import string
length = 10
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print('The password is:', password)
p= string.ascii_uppercase + string.ascii_uppercase + string.digits + string.punctuation + string.ascii_letters
