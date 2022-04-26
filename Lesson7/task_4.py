import os
import json

if __name__ == '__main__':

    folder = os.path.join(os.path.curdir, 'some_data')
    if not os.path.exists(folder):
        raise FileNotFoundError

    stat = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            size = os.stat(os.path.join(root,file)).st_size
            num_sum = 0
            while size:
                num_sum += 1
                size //= 10
            num_sum = 10 ** num_sum
            if num_sum not in stat:
                stat[num_sum] = 0
            stat[num_sum] += 1

    print(json.dumps(stat, sort_keys=True, indent=2))
