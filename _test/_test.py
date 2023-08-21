from DB.sqlite import Db

db = Db()
query = db.view_dates()
dates = [row[0] for row in query]

print(dates)