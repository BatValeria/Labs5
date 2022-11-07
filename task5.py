import string
import random

def get_random_password(len: int) -> str:
   list_ = random.sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=len)
   return "".join(list_)

print(get_random_password(8))

#string.digits and string.ascii_lowercase and string.ascii_lowercase