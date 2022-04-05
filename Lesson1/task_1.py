## Урок 1. Знакомство с Python
__author__ = "Худолей Артем Викторович"

# 1. Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
# a. до минуты: <s> сек;
# b. до часа: <m> мин <s> сек;
# c. до суток: <h> час <m> мин <s> сек;
# d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input("Введите время в секундах:"))
minute = 60
hour = minute * minute
day = hour * 24
hours = duration // 60 // 60
days = hours // 24
mod_hour = (duration - days * day) // hour
mod_min = (duration - (hours * hour)) // minute
mod_sec = duration % minute
if duration < minute:
    print(duration, "сек")
elif duration < hour:
    print(duration // 60, "мин", mod_sec, "сек")
elif duration < day:
    print(hours, "час", mod_min, "мин", mod_sec, "сек")
else:
    print(days, "д", mod_hour, "час", mod_min, "мин", mod_sec, "сек")
