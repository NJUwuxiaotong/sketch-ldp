import json
import math
import random

from pub_lib import hash_functions


PRIME_INT = int('1' * 61, 2)


def generate_random(num, f1_path, f2_path):
    x = []
    y = []

    for i in range(num):
        x.append([random.randint(1, PRIME_INT), random.randint(1, PRIME_INT)])
        y.append([random.randint(1, PRIME_INT), random.randint(1, PRIME_INT),
                  random.randint(1, PRIME_INT), random.randint(1, PRIME_INT)])

    with open(f1_path, 'w+') as f:
        json.dump(x, f)

    with open(f2_path, 'w+') as f:
        json.dump(y, f)


def test_mult_add_prime():
    pass




a = random.randint(1, PRIME_INT)
b = random.randint(1, PRIME_INT)
c = random.randint(1, PRIME_INT)
d = random.randint(1, PRIME_INT)

x = 111

print(x, a, b, c, d)
print(hash_functions.cw_trick_2(x, a, b))
print(hash_functions.cw_trick_4(x, a, b, c, d))

f1 = './paras_of_2_universal_hash_g.json'
f2 = './paras_of_4_universal_hash_g.json'
