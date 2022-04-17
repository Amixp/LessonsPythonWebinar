# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp.
from decimal import Decimal
import requests


def currency_rates(cur_code):
    """ Отдает курс по коду cur_code этой валюты по отношению к рублю"""
    values = {}
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    for i in r.text.split('<CharCode>')[1:]:
        value = Decimal(i.split('Value')[1].strip("<>/").replace(",", "."))
        values.setdefault(i[0:3], value)
    return values.get(cur_code.upper())


print(currency_rates("USD"))
print(currency_rates("eur"))
print(currency_rates("EUF"))

