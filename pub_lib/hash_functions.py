import bitarray


INT8_BIT_LEN = 8
INT16_BIT_LEN = 16
INT32_BIT_LEN = 32
INT64_BIT_LEN = 64

LOW_BIT_LEN = 32
PRIME_BIT_LEN = 61
STR_BIT_TRUE = '1'
STR_BIT_FALSE = '0'

PRIME_INT = int('1' * 61, 2)

LOWONES = bitarray.bitarray('1' * LOW_BIT_LEN)
PRIME_STR = bitarray.bitarray('0' * (INT64_BIT_LEN - PRIME_BIT_LEN) +
                              '1' * PRIME_BIT_LEN)


def map_int_to_64(x):
    """
    :param x: int
    :return: 64-bit array {0,1}
    """
    x = bin(x)[2:]
    x_len = len(x)
    x = (INT64_BIT_LEN - x_len) * '0' + x
    return x


def low_32_from_64(x):
    """
    :param x: 64-bit
    :return: '0'/'1'
    """
    x_bin = map_int_to_64(x)
    return x_bin[32:]


def high_32_from_64(x):
    """
    :param x: 64-bit
    :return: '0'/'1'
    """
    x_bin = map_int_to_64(x)
    return x_bin[:32]


def int_and_prime(x):
    y = bin(x)[2:]
    y_len = len(y)
    if y_len >= PRIME_BIT_LEN:
        y = y[-1 * PRIME_BIT_LEN:]
    return int(y, 2)


def mult_add_prime(x, a, b):
    """
    :param x: 32-bit
    :param a: 64-bit
    :param b: 64-bit
    :return:
    """
    a0 = int(low_32_from_64(a), 2) * x
    a1 = int(high_32_from_64(a), 2) * x
    c0 = a0 + int(bin(a1) + '0' * 32, 2)
    c1 = int(bin(a0)[:-32], 2) + a1

    c = int_and_prime(c0) + int(bin(c1)[:-29], 2) + b
    return c


def cw_trick_2(x, a, b):
    # CW Trick for 32-bit keys with prime 2^61-1
    h = mult_add_prime(x, a, b)
    h_64 = map_int_to_64(h)

    t0 = bitarray.bitarray(h_64)
    t1 = PRIME_STR & t0
    h0 = t1.to01()

    h = int(h0, 2) + int(h_64[61:], 2)
    if h >= PRIME_INT:
        h -= PRIME_INT
    return h


def cw_trick_4(x, a, b, c, d):
    h = mult_add_prime(mult_add_prime(mult_add_prime(x, a, b), x, c), x, d)
    h_64 = map_int_to_64(h)

    t0 = bitarray.bitarray(h_64)
    t1 = PRIME_STR & t0
    h0 = t1.to01()

    h = int(h0, 2) + int(h_64[61:], 2)
    if h >= PRIME_INT:
        h -= PRIME_INT
    return h
