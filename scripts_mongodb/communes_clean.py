import tools as t

name_db = "demo_mongo"
name_coll = "communes"

client = t.getMongoClient()

t.printLog(f"Drop database : [{name_db}]")
client.drop_database(name_db)




