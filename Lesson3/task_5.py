# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого):
import random


def get_jokes(n, uniq_joke=False):
    """ Возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков
        если флаг uniq_joke, то запрещается повтор слов в шутках
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    sp = " "
    if uniq_joke:
        for joke in range(n):
            s1 = random.choice(nouns)
            s2 = random.choice(adverbs)
            s3 = random.choice(adjectives)

            nouns.remove(s1)
            adverbs.remove(s2)
            adjectives.remove(s3)

            jokes.append(sp.join((s1, s2, s3)))
    else:
        for joke in range(n):
            jokes.append(sp.join([str(random.choice(nouns)), random.choice(adverbs), random.choice(adjectives)]))
    return jokes


print(get_jokes(3, uniq_joke=True))
print(get_jokes(3))
