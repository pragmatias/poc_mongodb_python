import json
import tools as t

dir_data = f"{t.dir_root}/data/genere/cities"
file_data = f"{dir_data}/communes.json"

name_db = "demo_mongo"
name_coll = "communes"


client = t.getMongoClient()

t.printLog(f"Use Database : [{name_db}]")
mongo_db = client[name_db]
mongo_col = mongo_db[name_coll]

res_coll_count = mongo_col.count_documents(filter={},limit=1)

if (res_coll_count == 0):
    # Read json data
    with open(file_data,"r") as f :
        import_data = json.load(f)
    
    res_insert = mongo_col.insert_many(import_data)
    t.printLog(f"[{len(res_insert.inserted_ids)}] documents have been inserted in [{name_db}.{name_coll}] !")
else :
    t.printLog(f"Collection [{name_db}.{name_coll}] is not empty !")





