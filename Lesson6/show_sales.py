import sys
from constants import COST_LEN


if __name__ == '__main__':
    start_pos = 0
    stop_pos = 0
    if len(sys.argv) >= 2:
        start_pos = sys.argv[1]
    if len(sys.argv) >= 3:
        stop_pos = sys.argv[2]

    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if not start_pos and not stop_pos:
            bakery = f.read()
            print(bakery)
        if start_pos:
            if not start_pos.isnumeric():
                print("Начальная позиция не указана числом")
        if stop_pos:
            if not stop_pos.isnumeric():
                print("Конечная позиция не указана числом")
        bakery = ""
        cur_pos = 0
        f.seek((COST_LEN+1)*(int(start_pos)-1))
        for line in f:
            bakery += line
            cur_pos += len(line) + 1
            if stop_pos:
                if cur_pos > (COST_LEN*int(stop_pos)):
                    break
        print(bakery)
