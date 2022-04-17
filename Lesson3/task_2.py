# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.

def num_translate_adv(number_word):
    num_word = {'null': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    _ = num_word.get(number_word.lower())
    if number_word.istitle():
        return _.title()
    return _


print(num_translate_adv("One"))
print(num_translate_adv("Nine"))
