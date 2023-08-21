from DB.sqlite import Db


db = Db()
count = 0
for i in range (1, 735):
    query_name = db.select_phonebook_id(i)
    print(query_name[0][0], query_name[0][6][3:])
    count += 1
    if query_name[0][0] != query_name[0][6][3:]:
        print(count, False)

print("Сравнение окончено")
