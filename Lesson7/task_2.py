# 2. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
import os
import yaml


def mkdirs(cur_dir, item):
    if isinstance(item, dict):
        for key, value in item.items():
            if not os.path.exists(os.path.join(cur_dir, key)):
                print(f'mkdir {os.path.join(cur_dir, key)}')
                os.mkdir(os.path.join(cur_dir, key))
            mkdirs(os.path.join(cur_dir, key), value)
    elif isinstance(item, list):
        for item in item:
            mkdirs(cur_dir, item)
    else:
        if item:
            full_name = os.path.join(cur_dir, item)
            if not os.path.exists(full_name):
                print(f'touch {full_name}')
                with open(full_name, 'a'):
                    pass


profile = """
    my_project:
      settings:
        - __init__.py
        - dev.py
        - prod.py
      mainapp:
        - __init__
        - models.py
        - views.py
        - templates:
          - mainapp:
            - base.html
            - index.html
      authapp: 
        - __init__.py   
        - models.py      
        - views.py
        - templates:
          - mainapp:
            - base.html
            - index.html
    """
if os.path.exists('config.yaml'):
    with open("config.yaml", "r") as stream:
        try:
            project = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
else:
    project = yaml.safe_load(profile)

mkdirs(os.path.curdir, project)
