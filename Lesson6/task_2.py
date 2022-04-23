# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания

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

clients = [address[0] for address in client_params]
'''Выбираем список только IP адресов клиентов'''

cl_conn = {address: clients.count(address) for address in set(clients)}
'''Тут уже словарь адресов с кол-вом повторений их в предыдушем списке'''

max_connections = 1000
'''Отбираем самые большие повторения'''
hackers = [str(hacker) + str(": ") + str(connections) for hacker, connections in list(cl_conn.items()) if connections > max_connections]
print(hackers)
