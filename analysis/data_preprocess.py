def map_v_to_n(keys):
    mappings = dict()
    reverse_map = dict()
    num = 0
    for k in keys:
        num += 1
        mappings[k] = num
        reverse_map[num] = k
    return mappings, reverse_map
