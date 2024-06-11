import json
import tools_azcosmosdb as ac
from azure.cosmos import CosmosClient, PartitionKey, SSLConfiguration

dir_data = ac.dir_data_json
file_data = f"{ac.dir_data_json}/communes.json"

client = ac.getCosmosClient()
import_data = []

local_conf = {
    "database" : "demo-db"
}

# Create the database if not exists
database = client.create_database_if_not_exists(
    id=local_conf["database"],
    offer_throughput=400,
)


# container = table
container = database.create_container_if_not_exists(
    id="communes",
    partition_key=PartitionKey(
        path="/code",
    ),
)

# Read json data
with open(file_data,"r") as f :
    import_data = json.load(f)

# browse json object from array and write item in the container
for elt in import_data:
    elt["id"] = elt["code"]
    container.upsert_item(elt)


print(f"Data writen in the container [communes] in the database [{local_conf['database']}]")


