import json
import numpy as np

from algs.cms_ldp import CMSLDP
from algs.fcs_ldp import FCSLDP
from algs.cs_ldp import CSLDP
from algs.fas_ldp import FASLDP
from analysis import data_preprocess
from log.logger import Logger


LOG = Logger(level='debug').logger

OD_PATH = 'F:\\busyfish\paper\computer communications March 15\experi' \
          'ments\sketch-ldp\datasets\OD_dataset.json'
WISDOM_PATH = 'F:\\busyfish\paper\computer communications March 15\experi' \
              'ments\sketch-ldp\datasets\WISDOM_dataset.json'
RESULT_DIR = '../result/'


with open(OD_PATH, 'r+') as f:
    od = json.load(f)

with open(WISDOM_PATH, 'r+') as f:
    wisdom = json.load(f)

od_mappings, od_reverse_map = data_preprocess.map_v_to_n(od)
wisdom_mappings, wisdom_reverse_map = data_preprocess.map_v_to_n(wisdom)

with open(RESULT_DIR+'od_mappings.json', 'w+') as f:
    json.dump(od_mappings, f)

with open(RESULT_DIR+'wisdom_mappings.json', 'w+') as f:
    json.dump(wisdom_mappings, f)

od_keys = list(od_reverse_map.keys())
wisdom_keys = list(wisdom_reverse_map.keys())


def test_privacy_of_wisdom_cms_ldp():
    error_p = 0.18
    confidence = 0.1
    att_num = len(wisdom_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in wisdom:
        for i in range(int(wisdom[k]/50)):
            data.append(wisdom_mappings[k])

    LOG.info('Process dataset WISDOM')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter privacy_budget is %s' % privacy_budget)
        estimated_values = dict()
        cms = CMSLDP(data, error_p, confidence, privacy_budget, att_num)
        cms.sketch_cms_ldp()
        LOG.info(cms.sketch)
        for id in wisdom_mappings.values():
            estimated_values[id] = cms.server_cms_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


def test_privacy_of_wisdom_fcs_ldp():

    error_p = 0.18
    confidence = 0.1
    att_num = len(wisdom_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in wisdom:
        for i in range(int(wisdom[k]/50)):
            data.append(wisdom_mappings[k])

    LOG.info('Process dataset WISDOM - FCS-LDP')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter privacy_budget is %s' % privacy_budget)
        estimated_values = dict()
        fcs = FCSLDP(data, error_p, confidence, privacy_budget, att_num)
        fcs.sketch_fcs_ldp()
        LOG.info(fcs.sketch)
        for id in wisdom_mappings.values():
            estimated_values[id] = fcs.server_fcs_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


def test_privacy_of_wisdom_cs_ldp():
    error_p = 0.18
    confidence = 0.1
    att_num = len(wisdom_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in wisdom:
        for i in range(int(wisdom[k]/50)):
            data.append(wisdom_mappings[k])

    LOG.info('Process dataset WISDOM - CS-LDP')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter privacy_budget is %s' % privacy_budget)
        estimated_values = dict()
        cs = CSLDP(data, error_p, confidence, privacy_budget, att_num)
        cs.sketch_cs_ldp()
        LOG.info(cs.sketch)
        for id in wisdom_mappings.values():
            estimated_values[id] = cs.server_cs_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


def test_privacy_of_wisdom_fas_ldp():
    error_p = 0.18
    confidence = 0.1
    att_num = len(wisdom_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in wisdom:
        for i in range(int(wisdom[k]/50)):
            data.append(wisdom_mappings[k])

    LOG.info('Process dataset WISDOM - FAS-LDP')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter confidence is %s' % confidence)
        estimated_values = dict()
        cs = FASLDP(data, error_p, confidence, privacy_budget, att_num)
        cs.sketch_fas_ldp()
        LOG.info(cs.sketch)
        for id in wisdom_mappings.values():
            estimated_values[id] = cs.server_fas_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


def test_privacy_of_od_cms_ldp():
    error_p = 0.005
    confidence = 0.1
    att_num = len(od_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in od:
        for i in range(int(od[k]/50)):
            data.append(od_mappings[k])

    LOG.info('Process dataset OD')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter privacy_budget is %s' % privacy_budget)
        estimated_values = dict()
        cms = CMSLDP(data, error_p, confidence, privacy_budget, att_num)
        cms.sketch_cms_ldp()
        LOG.info(cms.sketch)
        for id in od_mappings.values():
            estimated_values[id] = cms.server_cms_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


def test_privacy_of_od_fcs_ldp():
    error_p = 0.005
    confidence = 0.1
    att_num = len(od_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in od:
        for i in range(int(od[k]/50)):
            data.append(od_mappings[k])

    LOG.info('Process dataset OD - FCS-LDP')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter privacy_budget is %s' % privacy_budget)
        estimated_values = dict()
        fcs = FCSLDP(data, error_p, confidence, privacy_budget, att_num)
        fcs.sketch_fcs_ldp()
        LOG.info(fcs.sketch)
        for id in od_mappings.values():
            estimated_values[id] = fcs.server_fcs_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


def test_privacy_of_od_cs_ldp():
    error_p = 0.005
    confidence = 0.1
    att_num = len(od_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in od:
        for i in range(int(od[k]/50)):
            data.append(od_mappings[k])

    LOG.info('Process dataset OD - CS-LDP')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter privacy_budget is %s' % privacy_budget)
        estimated_values = dict()
        cs = CSLDP(data, error_p, confidence, privacy_budget, att_num)
        cs.sketch_cs_ldp()
        LOG.info(cs.sketch)
        for id in od_mappings.values():
            estimated_values[id] = cs.server_cs_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


def test_privacy_of_od_fas_ldp():
    error_p = 0.005
    confidence = 0.1
    att_num = len(od_keys)

    privacy_budgets = [1, 3, 5, 7]
    data = list()
    for k in od:
        for i in range(int(od[k]/50)):
            data.append(od_mappings[k])

    LOG.info('Process dataset OD - FAS-LDP')
    for privacy_budget in privacy_budgets:
        LOG.info('Parameter privacy_budget is %s' % privacy_budget)
        estimated_values = dict()
        cs = FASLDP(data, error_p, confidence, privacy_budget, att_num)
        cs.sketch_fas_ldp()
        LOG.info(cs.sketch)
        for id in od_mappings.values():
            estimated_values[id] = cs.server_fas_ldp(id)
        LOG.info('Frequency estimation is %s' % estimated_values)


test_privacy_of_wisdom_cms_ldp()
test_privacy_of_wisdom_fcs_ldp()
test_privacy_of_wisdom_cs_ldp()
test_privacy_of_wisdom_fas_ldp()

test_privacy_of_od_cms_ldp()
test_privacy_of_od_fcs_ldp()
test_privacy_of_od_cs_ldp()
test_privacy_of_od_fas_ldp()
