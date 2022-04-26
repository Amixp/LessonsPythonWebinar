import os
import random

folder = os.path.join(os.path.curdir,'some_data')
if not os.path.exists(folder):
    os.makedirs(folder)
letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
for _ in range(10 ** 3):
    f_name = ''.join(random.sample(letters, random.randint(5, 10)))
    f_content = bytes(random.randint(0, 255)
                      for _ in range(random.randrange(10 ** 5)))
    with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
        f.write(f_content)
