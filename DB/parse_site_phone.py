import requests


def parse_site():
    url = "http://bgu.ru/about/phonebook.aspx"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}
    query = requests.get(url, headers=headers)

    with open('DB\Phonebook.html', 'w', encoding="utf-8") as file:
        file.write(query.text)

parse_site()