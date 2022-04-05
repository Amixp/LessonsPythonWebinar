__author__ = "Худолей Артем Викторович"

# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
# числа X):
# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!
# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7.
# c. * Решить задачу под пунктом b, не создавая новый список.

list_nums = range(1, 1001, 2)
list_kub = []

sums1 = 0
sums2 = 0
for idx, item in enumerate(list_nums):
    list_kub.append(item ** 3)

    num_sum = 0
    number = list_kub[idx]
    while number:
        num_sum += number % 10
        number = number // 10
    if num_sum % 7 == 0:
        sums1 += list_kub[idx]

    num_sum = 0
    number = list_kub[idx]+17
    while number:
        num_sum += number % 10
        number = number // 10
    if num_sum % 7 == 0:
        sums2 += list_kub[idx]+17

print(sums1, sums2, sep='\n')
