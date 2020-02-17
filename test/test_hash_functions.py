import json
import math
import random

from pub_lib import hash_functions


PRIME_INT = int('1' * 61, 2)

a = random.randint(1, PRIME_INT)
b = random.randint(1, PRIME_INT)
c = random.randint(1, PRIME_INT)
d = random.randint(1, PRIME_INT)

x = 111

print(x, a, b, c, d)
print(hash_functions.cw_trick_2(x, a, b))

print(hash_functions.cw_trick_4(x, a, b, c, d))

f1 = './parameters_of_2_universal_hash_functions.json'
f2 = './parameters_of_4_universal_hash_functions.json'

