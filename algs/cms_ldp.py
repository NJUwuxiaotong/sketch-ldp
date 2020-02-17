import json
import math
import numpy as np
import random

from algs.sketch_ldp import SketchLDP
from pub_lib import hash_functions


class CMSLDP(SketchLDP):
    def __init__(self, data, error_p, confidence, privacy):
        """
        :param data: a list
        :param error_p:
        :param confidence:
        :param privacy:
        """
        super(CMSLDP, self).__init__(data, error_p, confidence, privacy)
        self.file_path_of_hash = \
            '../constants/parameters_of_2_universal_hash_functions.json'
        self.total_hash_num = 100
        self.hash_index = []
        self.hash_parameters = []
        self.data_len = len(data)
        self.bit_len = math.ceil(2 / self.error_p)
        self.hash_num = math.ceil(math.log2(1 / self.confidence))
        self.generate_hash_index(self.hash_num)
        self.get_parameters_of_hash()

    def generate_hash_index(self, hash_num):
        hash_index = []
        while len(hash_index) <= hash_num:
            h_index = random.randint(0, self.total_hash_num - 1)
            if h_index not in hash_index:
                hash_index.append(h_index)
        self.hash_index = hash_index

    def get_parameters_of_hash(self):
        with open(self.file_path_of_hash, 'r+') as f:
            parameters = json.load(f)
        for i in range(self.hash_num):
            self.hash_parameters.append(parameters[self.hash_index[i]])

    def get_frequency_estimation(self):
        for i in range(self.data_len):
            pass

    def client_cms_ldp(self, element):
        sub_privacy = self.privacy/self.hash_num
        values = np.zeros([self.hash_num, self.bit_len])
        for i in range(self.hash_num):

            pos = hash_functions.cw_trick_2()

    def sketch_cms_ldp(self):
        pass

    def server_cms_ldp(self):
        pass
