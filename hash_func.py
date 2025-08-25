import hashlib
import random
import string


def random_string(length=32):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])


def find_hash(attempts=1000):
    for _ in range(attempts):
        s = random_string()
        h = hashlib.md5(s.encode()).hexdigest()

        if h[:2] == "00":
            return True
    
    return False