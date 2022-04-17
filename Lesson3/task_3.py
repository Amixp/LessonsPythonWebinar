# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
names = "Роман", "Никита", "Иван", "марина", "Алексей", "андрей", "марья", "оля", "Мария", "Петр", "Илья"


def up_first_ch(el):
    return el[0].upper()


def thesaurus(list_names):
    dict_names = {}
    for n in list_names:
        dict_names.setdefault(up_first_ch(n), list())
        dict_names[up_first_ch(n)].append(n)
    return dict_names


print(thesaurus(names))

the_dict = thesaurus(names)
for nm in sorted(the_dict):
    print(nm, the_dict[nm])

