"""
Задание  1.
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""
import requests
# import json
from pprint import pprint

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/66.0.3359.181 Chrome/66.0.3359.181 Safari/537.36'
github_api_url = 'https://api.github.com/users/'

user_name = 'GefMar'
repos = '/repos'

response = requests.get(f'{github_api_url}{user_name}{repos}', params={'sort': 'mi+n мач','start': 1}, headers={'User_Agent': USER_AGENT})
data = response.json()

# for key, value in data.items():
#     print(f'{key} - {value}')
# print(data)

pprint(response.text)
file = open('d:\out.json', 'w')
file.write(str(response.json()))
response.close()