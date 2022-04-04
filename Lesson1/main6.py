i = 0
while True:
    i += 1
    if i >= 10:
        break  # выход из цикла
    if i % 2 == 0:
        continue  # вернуться к while
    print(i)
