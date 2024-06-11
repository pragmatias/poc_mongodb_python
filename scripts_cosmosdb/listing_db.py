import json
import tools_azcosmosdb as ac
from azure.cosmos import CosmosClient, PartitionKey, SSLConfiguration


client = ac.getCosmosClient()

# listing database
listing_databases = list(client.list_databases())
print(f"########"*5)
print(f"Listing databases : {len(listing_databases)}")
print(f"########"*5)

for database in listing_databases:
    print(f"Database : {database['id']}")
    print(json.dumps(database,indent=2))



for database in listing_databases :
    containers = list(client.get_database_client(database["id"]).list_containers())
    print(f"Database : {database['id']} with [{len(containers)}] containers")
    for cont in containers:
        print(f"\tContainer : {cont['id']}")
        print(json.dumps(cont,indent=2))
    
    users = list(client.get_database_client(database["id"]).list_users())
    for us in users : 
        print("User : ")
        print(json.dumps(us,indent=2))
    













# Delete databases
#if len(listing_databases) > 0 :
#    list_db_suppr = list(map(lambda x:x["id"],listing_databases))
#    print(list_db_suppr)
#    for elt in list_db_suppr:
#        client.delete_database(elt)







