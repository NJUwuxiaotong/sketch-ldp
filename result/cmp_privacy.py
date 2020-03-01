import json
import math

from analysis import data_preprocess
from analysis import output_privacy_wisdom
from analysis import output_privacy_od

WISDOM_PATH = 'F:\\busyfish\paper\computer communications March 15\experi' \
              'ments\sketch-ldp\datasets\WISDOM_dataset.json'
WISDOM_MAPPING_PATH = 'F:\\busyfish\paper\computer communications March 15\ex' \
                      'periments\sketch-ldp\\result\wisdom_mappings.json'

OD_PATH = 'F:\\busyfish\paper\computer communications March 15\experi' \
          'ments\sketch-ldp\datasets\OD_dataset.json'
OD_MAPPING_PATH = 'F:\\busyfish\paper\computer communications March 15\ex' \
                  'periments\sketch-ldp\\result\od_mappings.json'

with open(WISDOM_PATH, 'r+') as f:
    wisdom = json.load(f)

with open(OD_PATH, 'r+') as f:
    od = json.load(f)

od_mappings, od_reverse_map = data_preprocess.map_v_to_n(od)
wisdom_mappings, wisdom_reverse_map = data_preprocess.map_v_to_n(wisdom)

wisdom_key_len = len(wisdom_mappings)  # key --> 18
od_key_len = len(od_mappings)          # key --> 621


# RE for wisdom
# param: error --> [0.15, 0.18, 0.2, 0.25], top-18
# cms
def get_wisdom_cms():
    wisdom_cms = output_privacy_wisdom.WISDOM_PRIVACY_CMS
    cms_re = []
    cms_mse = []
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(1, wisdom_key_len+1):
            tmp += math.fabs(math.fabs(wisdom_cms[i][j]) - wisdom[wisdom_reverse_map[j]]/50)\
                   / (wisdom[wisdom_reverse_map[j]]/50)
            v += math.pow(math.fabs(wisdom_cms[i][j]) - wisdom[wisdom_reverse_map[j]]/50, 2)
        tmp = tmp / wisdom_key_len
        v = v / wisdom_key_len
        cms_re.append(tmp*50)
        cms_mse.append(v*50*50)
    return cms_re, cms_mse


# fcs
def get_wisdom_fcs():
    wisdom_fcs = output_privacy_wisdom.WISDOM_PRIVACY_FCS
    fcs_re = []
    fcs_mse = []
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(1, wisdom_key_len+1):
            tmp += math.fabs(math.fabs(wisdom_fcs[i][j]) - wisdom[wisdom_reverse_map[j]]/50)\
                   / (wisdom[wisdom_reverse_map[j]]/50)
            v += math.pow(math.fabs(wisdom_fcs[i][j]) - wisdom[wisdom_reverse_map[j]]/50, 2)
        tmp = tmp / wisdom_key_len
        v = v / wisdom_key_len
        fcs_re.append(tmp*50)
        fcs_mse.append(v * 50 * 50)
    return fcs_re, fcs_mse


# cs
def get_wisdom_cs():
    wisdom_cs = output_privacy_wisdom.WISDOM_PRIVACY_CS
    cs_re = []
    cs_mse = []
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(1, wisdom_key_len+1):
            tmp += math.fabs(math.fabs(wisdom_cs[i][j]) - wisdom[wisdom_reverse_map[j]]/50)\
                   / (wisdom[wisdom_reverse_map[j]]/50)
            v += math.pow(math.fabs(wisdom_cs[i][j]) - wisdom[wisdom_reverse_map[j]]/50, 2)
        tmp = tmp / wisdom_key_len
        v = v / wisdom_key_len
        cs_re.append(tmp*50)
        cs_mse.append(v*50*50)
    return cs_re, cs_mse


# fas
def get_wisdom_fas():
    wisdom_fas = output_privacy_wisdom.WISDOM_PRIVACY_FAS
    fas_re = []
    fas_mse = []
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(1, wisdom_key_len+1):
            tmp += math.fabs(math.fabs(wisdom_fas[i][j]) - wisdom[wisdom_reverse_map[j]]/50)\
                   / (wisdom[wisdom_reverse_map[j]]/50)
            v += math.pow(math.fabs(wisdom_fas[i][j]) - wisdom[wisdom_reverse_map[j]]/50, 2)
        tmp = tmp / wisdom_key_len
        v = v / wisdom_key_len
        fas_re.append(tmp*50)
        fas_mse.append(v*50*50)
    return fas_re, fas_mse


def get_top_k(k):
    od_sorted_key = []
    src_keys = list(od.keys())
    src_values = list(od.values())
    values = list(od.values())
    values.sort()
    values.reverse()
    for i in range(k):
        x = src_values.count(values[i])
        start_pos = 0
        for j in range(x):
            pos = src_values.index(values[i], start_pos)
            od_sorted_key.append(src_keys[pos])
            start_pos = pos + 1
    return od_sorted_key


def get_od_cms(ele_num):
    od_cms = output_privacy_od.OD_PRIVACY_CMS
    cms_re = []
    cms_mse = []
    od_keys = get_top_k(ele_num)
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(ele_num):
            id = od_mappings[od_keys[j]]

            tmp += math.fabs(math.fabs(od_cms[i][id]) - od[od_keys[j]] / 50) \
                   / (od[od_keys[j]] / 50)
            v += math.pow(math.fabs(od_cms[i][id]) - od[od_keys[j]] / 50, 2)
        tmp = tmp / ele_num
        v = v / ele_num
        cms_re.append(tmp * 50)
        cms_mse.append(v * 50 * 50)
    return cms_re, cms_mse


def get_od_fcs(ele_num):
    od_fcs = output_privacy_od.OD_PRIVACY_FCS
    fcs_re = []
    fcs_mse = []
    od_keys = get_top_k(ele_num)
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(ele_num):
            id = od_mappings[od_keys[j]]

            tmp += math.fabs(math.fabs(od_fcs[i][id]) - od[od_keys[j]] / 50) \
                   / (od[od_keys[j]] / 50)
            v += math.pow(math.fabs(od_fcs[i][id]) - od[od_keys[j]] / 50, 2)
        tmp = tmp / ele_num
        v = v / ele_num
        fcs_re.append(tmp * 50)
        fcs_mse.append(v * 50 * 50)
    return fcs_re, fcs_mse


def get_od_cs(ele_num):
    od_cs = output_privacy_od.OD_PRIVACY_CS
    cs_re = []
    cs_mse = []
    od_keys = get_top_k(ele_num)
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(ele_num):
            id = od_mappings[od_keys[j]]

            tmp += math.fabs(math.fabs(od_cs[i][id]) - od[od_keys[j]] / 50) \
                   / (od[od_keys[j]] / 50)
            v += math.pow(math.fabs(od_cs[i][id]) - od[od_keys[j]] / 50, 2)
        tmp = tmp / ele_num
        v = v / ele_num
        cs_re.append(tmp * 50)
        cs_mse.append(v * 50 * 50)
    return cs_re, cs_mse


def get_od_fas(ele_num):
    od_fas = output_privacy_od.OD_PRIVACY_FAS
    fas_re = []
    fas_mse = []
    od_keys = get_top_k(ele_num)
    for i in range(4):
        tmp = 0
        v = 0
        for j in range(ele_num):
            id = od_mappings[od_keys[j]]

            tmp += math.fabs(math.fabs(od_fas[i][id]) - od[od_keys[j]] / 50) \
                   / (od[od_keys[j]] / 50)
            v += math.pow(math.fabs(od_fas[i][id]) - od[od_keys[j]] / 50, 2)
        tmp = tmp / ele_num
        v = v / ele_num
        fas_re.append(tmp * 50)
        fas_mse.append(v * 50 * 50)
    return fas_re, fas_mse


# print(get_wisdom_cms())
# print(get_wisdom_fcs())
# print(get_wisdom_cs())
# print(get_wisdom_fas())

print(get_od_cms(30))
print(get_od_fcs(30))
print(get_od_cs(30))
print(get_od_fas(30))
