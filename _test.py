from DB.sqlite import Db


db = Db()
query = db.select_phonebook_id(10)
# ids = [str(row[0]) for row in query]

print((str(query[0])), type(str(query[0])))


# for item in ids:
#     print(item)
