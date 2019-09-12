""""
Задание 2
Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
"""
import requests
AccesToken = 'Здесь_надо_указать_токен'

authentication = {'Authorization': 'token ' + AccesToken}

response = requests.get('https://api.github.com/user', headers=authentication)
response.json()
file = open('d:\with_autoriz_repo.json', 'w')
file.write(str(response.json()))
file.close()
response.close()