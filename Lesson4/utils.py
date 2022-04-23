# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp.
from requests import get
from decimal import Decimal


def currency_rates(cur_code):
    """ Отдает курс по коду cur_code этой валюты по отношению к рублю"""
    values = {}
    r = get('http://www.cbr.ru/scripts/XML_daily.asp')
    for i in r.text.split('<CharCode>')[1:]:
        value = Decimal(i.split('Value')[1].strip("<>/").replace(",", "."))
        values.setdefault(i[0:3], value)
    return values.get(cur_code.upper())


if __name__ == '__main__':
    import sys
    """ печатает в консоль курс по коду из первого параметра """
    print(currency_rates(sys.argv[1]))
    exit(0)
