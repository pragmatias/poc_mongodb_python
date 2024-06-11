import tools as tm
from bson import json_util as bson

name_db = "demo_mongo"
name_coll = "communes"

client = tm.getMongoClient()

# Check if database exist
db_exist = name_db in list(client.list_database_names())
if db_exist:
    print(f"Database [{name_db}] exist !")
else:
    raise Exception(f"Database [{name_db}] doesn't exist !")
    exit(1) 

db = client[name_db]

# Check if collection exist
coll_exist = name_coll in list(db.list_collection_names())
if coll_exist:
    print(f"Collection [{db.name}.{name_coll}] exist !")
else:
    raise Exception(f"Collection [{db.name}.{name_coll}] doesn't exist !")
    exit(1) 


coll = db[name_coll]

# Get one random result (first document in the collection)
x = coll.find_one()
print(f"Get one random result : \n{bson.dumps(x,indent=2)}")




# Get result with a complex query
myquery = { "$or" : [
                {"$and": [{ "codeDepartement": "91"}
                          ,{"population" : {"$gt":20000} }
                          ,{"nom":{"$regex":"^(?!.*Ulis.*)"}}] }
                ,{"$and": [{ "codeDepartement": "91"}
                           ,{"nom":{"$regex":".*Ulis.*"}}] }
                ] }
myquery_res = list(coll.find(myquery))
count_res = len(myquery_res)
message = f"Get result from complex query :"
print(f"{message} [{count_res}] matching documents.")

for res in myquery_res:
    print(bson.dumps(res))


# Update codeDepartement
res = coll.update_many(filter = {"codeDepartement" : "91"}
                       ,update = {"$set": {"codeDepartement" : "XX"}})
print(f"Update codeDepartement from 91 to XX : [{res.matched_count}] match - [{res.modified_count}] modification !")
countDepXX = coll.count_documents(filter={"codeDepartement":"XX"})
countDep91 = coll.count_documents(filter={"codeDepartement":"91"})
print(f"We have [{countDepXX}] documents for department XX")
print(f"We have [{countDep91}] documents for department 91")


res = coll.update_many(filter = {"codeDepartement" : "XX"}
                       ,update = {"$set": {"codeDepartement" : "91"}})
print(f"Update codeDepartement from XX to 91 : [{res.matched_count}] match - [{res.modified_count}] modification !")
countDepXX = coll.count_documents(filter={"codeDepartement":"XX"})
countDep91 = coll.count_documents(filter={"codeDepartement":"91"})
print(f"We have [{countDepXX}] documents for department XX")
print(f"We have [{countDep91}] documents for department 91")



res_find = coll.find_one(filter={"$and":[{"codeDepartement":"91"},{"nom":"Yerres"}]})
print(f"Existing value : [{res_find['population']}]")

res = coll.update_one(filter = {"$and":[{"codeDepartement":"91"},{"nom":"Yerres"}]}
                      ,update = {"$inc":{"population":10000}})
print(f"Add population into Yerres (91) : [{res.matched_count}] match - [{res.modified_count}] modification !")
res_find = coll.find_one(filter={"$and":[{"codeDepartement":"91"},{"nom":"Yerres"}]})
print(f"new value after Add : [{res_find['population']}]")

res = coll.update_one(filter = {"$and":[{"codeDepartement":"91"},{"nom":"Yerres"}]}
                      ,update = {"$inc":{"population":-10000}})
print(f"Suppr population into Yerres (91) : [{res.matched_count}] match - [{res.modified_count}] modification !")
res_find = coll.find_one(filter={"$and":[{"codeDepartement":"91"},{"nom":"Yerres"}]})
print(f"new value after Suppr : [{res_find['population']}]")




