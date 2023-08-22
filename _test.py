from DB.sqlite import Db


db = Db()
query = db.search_byname('Михаил')



for i in range(len(query)):
    id = str(query[i][0])
    name = query[i][1]
    print(id,name)
