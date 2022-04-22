# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
# что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями —
# запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения —
# данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби,
# меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
import sys
import json

users = 'users.csv'
hobbys = 'hobby.csv'
peoples = dict()

with open(users, 'r', encoding='utf-8') as fu:
    with open(hobbys, 'r', encoding='utf-8') as fh:
        while True:
            people = fu.readline().replace(',', ' ').rstrip('\n')
            hobby = fh.readline().rstrip('\n')
            if not people:
                if not hobby:
                    break
                else:
                    sys.exit(1)
            if not hobby:
                hobby = None
            peoples[people] = hobby

print(peoples)

json.dump(peoples, open("peoples.json", 'w'))

# Read data from file:
peoples = json.load(open("peoples.json"))

print(peoples)
