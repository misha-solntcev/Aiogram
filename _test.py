from DB.sqlite import Db


db = Db()
link = db.get_2gis_link(2)[0][0]
print(link)


query = db.view_dates()
dates = [row[0] for row in query]
query = db.search_bydate(dates[0])

for item in query:
    num_build = int(item[3].split('-')[0])
    print(num_build, type(num_build))