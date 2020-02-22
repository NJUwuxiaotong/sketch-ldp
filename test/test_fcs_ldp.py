import math
import random

from algs.fcs_ldp import FCSLDP


def test_random_generator():
    data = [1, 3, 5, 1, 3, 2, 4, 4]
    error_p = 0.2
    confidence = 0.1
    privacy = 2
    att_num = 5
    cms = FCSLDP(data, error_p, confidence, privacy, att_num)

    element = 2
    bit_len = cms.bit_len
    con = dict()
    for i in range(bit_len):
        con[i] = 0
    for i in range(10000):
        con[cms.random_generator(1, element)] += 1

    for i in range(bit_len):
        print('%s: %s' % (i, con[i]/10000))


def test_generate_hash():
    data = [1, 3, 5, 1, 3, 2, 4, 4]
    error_p = 0.1
    confidence = 0.1
    privacy = 2
    att_num = 5
    cms = FCSLDP(data, error_p, confidence, privacy, att_num)
    print(cms.hash_index)
    print(cms.hash_parameters)


def test_client_fcs_ldp():
    data = [1, 3, 5, 1, 3, 2, 4, 4]
    error_p = 0.1
    confidence = 0.1
    privacy = 2
    att_num = 5
    cms = FCSLDP(data, error_p, confidence, privacy, att_num)

    element = 2
    print(cms.client_fcs_ldp(element))


def test_sketch_fcs_ldp():
    data = [1, 3, 5, 1, 3, 2, 4, 4]
    error_p = 0.1
    confidence = 0.1
    privacy = 2
    att_num = 5
    cms = FCSLDP(data, error_p, confidence, privacy, att_num)
    cms.sketch_fcs_ldp()
    print(cms.sketch)


def test_server_fcs_ldp():
    data = []
    s = {1:0, 2:0, 3:0, 4:0, 5:0}
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
    cms = FCSLDP(data, error_p, confidence, privacy, att_num)
    cms.sketch_fcs_ldp()
    print(cms.server_fcs_ldp(1))
    print(cms.server_fcs_ldp(2))
    print(cms.server_fcs_ldp(3))
    print(cms.server_fcs_ldp(4))
    print(cms.server_fcs_ldp(5))


test_server_fcs_ldp()
