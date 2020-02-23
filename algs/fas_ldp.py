import json
import math
import numpy as np
import random

from algs.sketch_ldp import SketchLDP
from log.logger import Logger
from pub_lib import hash_functions

LOG = Logger(level='debug').logger


class FASLDP(SketchLDP):
    def __init__(self, data, error_p, confidence, privacy, att_num):
        super(FASLDP, self).__init__(data, error_p, confidence, privacy,
                                    att_num)
        self.file_path_of_hash_h = \
            '../constants/paras_of_2_universal_hash_h.json'
        self.file_path_of_hash_g = \
            '../constants/paras_of_4_universal_hash_g.json'
        self.total_hash_num = 100
        self.hash_index = []
        self.hash_h_parameters = []
        self.hash_g_parameters = []
        self.data_len = len(data)
        self.bit_len = math.ceil(2 / self.error_p)
        self.hash_num = math.ceil(math.log2(1 / self.confidence))
        self.generate_hash_index(self.hash_num)
        LOG.info('bit length: %s, hash number: %s' % (self.bit_len,
                                                      self.hash_num))
        LOG.info('hash index is %s' % self.hash_index)
        self.get_parameters_of_hash()
        self.sketch = np.zeros([self.hash_num, self.bit_len])

    def generate_hash_index(self, hash_num):
        hash_index = []
        while len(hash_index) < hash_num:
            h_index = random.randint(0, self.total_hash_num - 1)
            if h_index not in hash_index:
                hash_index.append(h_index)
        self.hash_index = hash_index

    def get_parameters_of_hash(self):
        with open(self.file_path_of_hash_h, 'r+') as f:
            parameters = json.load(f)
        for i in range(self.hash_num):
            self.hash_h_parameters.append(parameters[self.hash_index[i]])

        with open(self.file_path_of_hash_g, 'r+') as f:
            parameters = json.load(f)
        for i in range(self.hash_num):
            self.hash_g_parameters.append(parameters[self.hash_index[i]])

    def client_fas_ldp(self, element):
        sub_privacy = self.privacy/self.hash_num/2
        values = np.ones([self.hash_num, self.bit_len]) * -1
        for i in range(self.hash_num):
            h_para = self.hash_h_parameters[i]
            pos = hash_functions.cw_trick_2(
                element, h_para[0], h_para[1]) % self.bit_len
            g_para = self.hash_g_parameters[i]
            v = hash_functions.cw_trick_4(element, g_para[0], g_para[1],
                                          g_para[2], g_para[3]) % 2
            if v == 1:
                values[i][pos] = v

        for i in range(self.hash_num):
            for j in range(self.bit_len):
                r = self.random_generator(sub_privacy)
                values[i][j] = values[i][j] * r
        return values

    def sketch_fas_ldp(self):
        sub_privacy = self.privacy/self.hash_num/2
        c = (math.exp(sub_privacy) + 1)/(math.exp(sub_privacy) - 1)
        for i in range(self.data_len):
            values = self.client_fas_ldp(self.data[i])
            values = values * c
            self.sketch += values

    def server_fas_ldp(self, element):
        f = list()
        for i in range(self.hash_num):
            h_para = self.hash_h_parameters[i]
            pos = hash_functions.cw_trick_2(element, h_para[0], h_para[1])
            pos = pos % self.bit_len

            g_para = self.hash_g_parameters[i]
            v = hash_functions.cw_trick_4(element, g_para[0], g_para[1],
                                          g_para[2], g_para[3]) % 2
            if v == 0:
                v = -1
            f.append(self.bit_len*(
                    self.sketch[i][pos] * v - self.data_len/self.bit_len)/(
                    self.bit_len - 1))

        v_np = np.array(f)
        r = np.median(v_np)
        return math.ceil(r/self.hash_num)

    def random_generator(self, sub_privacy):
        e_privacy = math.exp(sub_privacy)
        p_positive = e_privacy/(e_privacy + 1)
        p_negative = 1/(e_privacy + 1)

        pos_norm = p_positive / (p_positive + p_negative)

        p = random.uniform(0, 1)
        if p < pos_norm:
            return 1
        else:
            return -1
