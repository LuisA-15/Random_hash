import hashlib
import random
import string

def random_string(length=32):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])

for i in range(1000):
    s = random_string()
    hash = hashlib.md5(s.encode()).hexdigest()

    if hash[:2] == "00":
        print("Hash found")
        print(hash)
        break