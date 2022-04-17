# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

def num_translate(number_word):
    num_word = {'null': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return num_word.get(number_word)


print(num_translate("one"))
print(num_translate("nine"))
print(num_translate("eleven"))

