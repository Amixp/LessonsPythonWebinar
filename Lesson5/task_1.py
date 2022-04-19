# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield

def odd_nums(max_num=1):
    for i in range(1, max_num+1, 2):
        yield i


odd_to_15 = odd_nums(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
