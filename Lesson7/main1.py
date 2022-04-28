import os
from collections import defaultdict
from os.path import relpath

root_dir = os.path.curdir
django_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(root, file), root_dir)
        django_files[ext].append(rel_path)

print('PY FILES')
print(*sorted(django_files['html'])[:10], sep='\n')
