from bs4 import BeautifulSoup
import requests
import sqlite3

with open("DB\_Phonebook.html", 'r', encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
rows = soup.find('div', class_='groups list-group bg-white').find_all('a')

href = []
for i in range(0, 1468, 2):
    href.append(rows[i].get('href'))

for i in range(len(href)):
    url = "http://bgu.ru/about/phonebook.aspx"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}
    query = requests.get(url=url + href[i], headers=headers)

    with open(f'DB\Phonebook\Phonebook{i}.html', 'w', encoding="utf-8") as file:
        file.write(query.text)
        print(f"Парсим страницу{i}")



