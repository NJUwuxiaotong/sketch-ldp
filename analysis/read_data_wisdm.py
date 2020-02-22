import json

import numpy as np


SAVE_FILE = 'F:\\busyfish\paper\computer communications March 15\exper' \
            'iments\sketch-ldp\datasets\WISDOM_dataset.json'
SAVE_ANALYSIS_FILE = 'F:\\busyfish\paper\computer communications March ' \
                     '15\experiments\sketch-ldp\datasets\WISDOM__analysis.json'


DATA = {"Walking": 886762, "Jogging": 862281, "Stairs": 841230,
        "Sitting": 875030,"Standing": 882587, "Typing": 833208,
        "Brush Teeth": 871710, "Eat Soup": 869704, "Eat Chips": 861398,
        "Eat Pasta": 840358, "Drinking": 901381, "Eat Sandwich": 857571,
        "Kicking": 882417, "Catch": 868766, "Dribblinlg": 882716,
        "Writing": 871159, "Clapping": 869905, "Fold Clothes": 872243}


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


analyze_data(DATA, SAVE_ANALYSIS_FILE)
save_data(DATA, SAVE_FILE)
