import random


def generate_random_str(size: int, base="QWERTYUIOPASDFGHJKLZXCVBNM"):
    result = ""
    for i in range(0, size):
        result += base[random.randint(0, len(base) - 1)]
    return result
