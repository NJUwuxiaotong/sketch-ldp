import json
import math
import numpy as np
import random

from algs.sketch_ldp import SketchLDP
from log.logger import Logger
from pub_lib import hash_functions

LOG = Logger(level='debug').logger


class CMSLDP(SketchLDP):
    def __init__(self, data, error_p, confidence, privacy, att_num):
        """
        :param data: a list
        :param error_p:
        :param confidence:
        :param privacy:
        """
        super(CMSLDP, self).__init__(data, error_p, confidence, privacy,
                                     att_num)
        self.file_path_of_hash = \
            '../constants/paras_of_2_universal_hash_h.json'
        self.total_hash_num = 100
        self.hash_index = []
        self.hash_parameters = []
        self.data_len = len(data)
        self.bit_len = math.ceil(2 / self.error_p)
        self.hash_num = math.ceil(math.log2(1 / self.confidence))
        LOG.info('bit length: %s, hash number: %s' % (self.bit_len,
                                                      self.hash_num))
        self.generate_hash_index(self.hash_num)
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
        with open(self.file_path_of_hash, 'r+') as f:
            parameters = json.load(f)
        for i in range(self.hash_num):
            self.hash_parameters.append(parameters[self.hash_index[i]])

    def client_cms_ldp(self, element):
        sub_privacy = self.privacy/self.hash_num
        values = np.zeros([self.hash_num, self.bit_len])
        for i in range(self.hash_num):
            para = self.hash_parameters[i]
            pos = hash_functions.cw_trick_2(
                element, para[0], para[1]) % self.bit_len
            y = self.random_generator(sub_privacy, pos)
            values[i][y] = 1
        return values

    def sketch_cms_ldp(self):
        for i in range(self.data_len):
            values = self.client_cms_ldp(self.data[i])
            self.sketch += values
        sub_privacy = self.privacy / self.hash_num
        e_privacy = math.exp(sub_privacy)
        p_positive = e_privacy / (e_privacy + self.bit_len - 1)
        p_negative = 1 / (e_privacy + self.bit_len - 1)
        q = p_positive/self.bit_len + \
            (self.bit_len - 1) * p_negative / self.bit_len
        self.sketch = (self.sketch - self.data_len*q)/(p_positive - q)

    def server_cms_ldp(self, element):
        f = list()
        for i in range(self.hash_num):
            para = self.hash_parameters[i]
            pos = hash_functions.cw_trick_2(element, para[0], para[1])
            pos = pos % self.bit_len
            f.append(self.sketch[i][pos])
        min_v = min(f)
        return math.ceil(min_v)

    def random_generator(self, sub_privacy, pos):
        e_privacy = math.exp(sub_privacy)
        p_positive = e_privacy/(e_privacy+self.bit_len-1)
        p_negative = 1/(e_privacy+self.bit_len-1)

        p_p = p_positive / (p_positive + p_negative * (self.bit_len - 1))
        p_q = p_negative / (p_positive + p_negative * (self.bit_len - 1))

        p = random.uniform(0, 1)
        if p < pos * p_q:
            return math.ceil(p/p_q) - 1

        if p < pos * p_q + p_p:
            return pos

        return pos + math.ceil((p - pos*p_q - p_p)/p_q)
