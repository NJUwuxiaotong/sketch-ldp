import csv
import json
import os

import numpy as np


ROOT_PATH = 'F:\\busyfish\paper\datasets\sketch-ldp-data\\boxi'
SAVE_FILE = 'F:\\busyfish\paper\computer communications March 15\exper' \
            'iments\sketch-ldp\datasets\OD_dataset.json'
SAVE_ANALYSIS_FILE = 'F:\\busyfish\paper\computer communications March ' \
                     '15\experiments\sketch-ldp\datasets\OD_analysis.json'


def get_all_files(f_path):
    if not os.path.exists(f_path):
        print('Error! The path %s does not exist' % f_path)
        exit(1)

    all_files = dict()
    # relative path
    for sub_dir in os.listdir(f_path):
        abs_path = f_path + '/' + sub_dir
        all_files[sub_dir] = os.listdir(abs_path)
    return all_files


def get_data(root_dir, all_files):
    """
    :param root_dir:
    :param all_files:
    :return: {key: num}
    """
    result = dict()
    total_num = 0

    for parent_dir, file_names in all_files.items():
        abs_dir = root_dir + '/' + parent_dir
        for file_name in file_names:
            f_path = abs_dir + '/' + file_name
            with open(f_path, 'r+') as f:
                f_csv = csv.reader(f)
                next(f_csv, None)
                for v in f_csv:
                    total_num += 1
                    value = int(v[0])
                    if value not in result:
                        result[value] = 1
                    else:
                        result[value] += 1
            print('End to process file %s' % f_path)
    return result


def analyze_data(result, dst_file):
    values = list(result.values())
    values = np.array(values)
    total_num = np.sum(values)
    min_v = np.min(values)
    max_v = np.max(values)
    avg_v = np.ceil(np.average(values))
    median_v = np.ceil(np.median(values))

    output = {"KEY_NUM": str(len(result)), "VALUE_NUM": str(total_num),
              "MIN": str(min_v), "MAX": str(max_v), "AVG": str(avg_v),
              "MEDIAN": str(median_v)}

    print(output)
    with open(dst_file, 'w+') as f:
        json.dump(output, f)


def save_data(result, dst_file):
    print('Start to save data to file %s' % dst_file)
    with open(dst_file, 'w+') as f:
        json.dump(result, f)
    print('End to save data to file %s' % dst_file)


fs = get_all_files(ROOT_PATH)
data = get_data(ROOT_PATH, fs)
analyze_data(data, SAVE_ANALYSIS_FILE)
save_data(data, SAVE_FILE)
