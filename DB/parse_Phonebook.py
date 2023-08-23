from bs4 import BeautifulSoup
import sqlite3

db = sqlite3.connect('DB\db.db')
cur = db.cursor()
if cur:
    print("Соединение установлено успешно")


# Создаем список ссылок
with open("DB\_Phonebook.html", 'r', encoding="utf-8") as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
rows = soup.find('div', class_='groups list-group bg-white').find_all('a')
href = []
for i in range(0, 1468, 2):
    href.append(rows[i].get('href'))


for i in range(len(href)):
    with open(rf"DB\Phonebook\Phonebook{i}.html", 'r', encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    res = soup.find('div', id="MainContent_divRezult").find_all('div', class_='col-lg-6 col-md-12')

    try:
        name = res[0].h4.text.strip()
    except:
        name = "None"
    try:
        position = res[0].p.text.strip()
    except:
        position = "None"
    try:
        department = " ".join((res[0].h5.text.strip()).split())
    except:
        department = "None"
    try:
        location = res[1].p.text.strip()
    except:
        location = "None"
    try:
        phone = res[1].find_all('p', class_='text-nowrap mr-4')[1].text.strip()
    except:
        phone = "None"
    try:
        email = res[1].find_all('p', class_='text-nowrap mr-4')[2].text.strip()
    except:
        email = "None"


    # Создаем таблицу
    cur.execute("""CREATE TABLE IF NOT EXISTS phonebook
                (id INTEGER PRIMARY KEY, name, position, department, location, phone, email, href)""")

    # Записываем данные в БД

    cur.execute("INSERT INTO phonebook VALUES (NULL,?,?,?,?,?,?,?)",
        (name, position, department, location, phone, email, href[i]))

    db.commit()
    print(f'Записана строка {i}')

db.close()
if not cur:
    print('Соединение закрыто')
