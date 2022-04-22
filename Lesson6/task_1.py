# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

f_name = 'nginx_logs.txt'
client_params = []
with open(f_name,'r', encoding='utf-8') as f:
    f.seek(0)
    while True:
        row = f.readline()
        if not row:
            break
        params = row.split()
        client_params.append((params[0], params[5].strip('"'), params[6]))

print(client_params)

