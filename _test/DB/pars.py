""" Берет расписание из файла Data.html спарсенного заранее
и помещает их в словарь schedule_dict где data - ключ,
значение - список параметров текущей лекции.
"""
import requests
from bs4 import BeautifulSoup
import sqlite3

with open("Data.html", 'r', encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
rows = soup.find_all("tr")

# Инициализация словаря
schedule_dict = {}

# Обход строк таблицы
for row in rows:
    # Проверка наличия даты
    date_row = row.find('td', colspan='4')
    if date_row is not None:
        date = date_row.text.strip() # key
        schedule_dict[date] = []
    
    # Получение данных о занятии
    time_row = row.find('td', class_='text-right text-nowrap')
    subject_row = row.find('span', class_='h5 text-oswald')
    lesson_type = row.find('td').find_next('td').contents[-1]
    location_row = row.find('td', class_='text-center')
    teacher_row = row.find('a')

    if time_row is not None:
        time = time_row.text.strip()
    if subject_row is not None:        
        subject = (" ".join((subject_row.text).split()))
    if lesson_type is not None:        
        lesson = (" ".join((lesson_type.text).split()))
    if location_row is not None:
        location = location_row.text.strip()
    if teacher_row is not None:        
        teacher = (" ".join((teacher_row.text).split()))
            
        # Добавление данных в словарь
        schedule_dict[date].append([time, subject, lesson, location, teacher])

# Вывод результата
for date, schedule in schedule_dict.items():
    print(date)
    
    print()

# data = schedule_dict['31 марта 2023 г. (Пятница)'] 

# print(*data, sep='\n')

