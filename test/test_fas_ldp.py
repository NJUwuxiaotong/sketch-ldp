import random

from algs.fas_ldp import FASLDP


def test_client_fas_ldp():
    data = [1, 3, 5, 1, 3, 2, 4, 4]
    error_p = 0.1
    confidence = 0.1
    privacy = 2
    att_num = 5
    cs = FASLDP(data, error_p, confidence, privacy, att_num)

    element = 2
    print(cs.client_fas_ldp(element))


def test_random_generator():
    data = [1, 3, 5, 1, 3, 2, 4, 4]
    error_p = 0.1
    confidence = 0.1
    privacy = 2
    att_num = 5
    cs = FASLDP(data, error_p, confidence, privacy, att_num)

    x = []
    for i in range(100):
        x.append(cs.random_generator(1))

    print(x.count(1))
    print(x.count(-1))


def test_sketch_fas_ldp():
    data = [1, 3, 5, 1, 3, 2, 4, 4]
    error_p = 0.1
    confidence = 0.1
    privacy = 2
    att_num = 5
    cms = FASLDP(data, error_p, confidence, privacy, att_num)
    cms.sketch_fas_ldp()
    print(cms.sketch)


def test_server_fas_ldp():
    data = []
    s = {1: 0, 2: 0, 3:0, 4:0, 5:0}
    for i in range(10000):
        r = random.randint(1, 5)
        data.append(r)
        s[r] += 1

    for i in range(5):
        print("%s" % (s[i+1]/10000.0))

    error_p = 0.2
    confidence = 0.1
    privacy = 2
    att_num = 5
    cms = FASLDP(data, error_p, confidence, privacy, att_num)
    cms.sketch_fas_ldp()
    print(cms.server_fas_ldp(1))
    print(cms.server_fas_ldp(2))
    print(cms.server_fas_ldp(3))
    print(cms.server_fas_ldp(4))
    print(cms.server_fas_ldp(5))


test_server_fas_ldp()
