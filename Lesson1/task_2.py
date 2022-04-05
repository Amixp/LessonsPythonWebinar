
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
