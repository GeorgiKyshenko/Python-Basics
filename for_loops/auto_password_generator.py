import string
import random

signs = string.ascii_letters + string.punctuation + string.digits
length = 12
current_password = "".join(random.sample(signs, length))
print(current_password)
