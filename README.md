# Project

POC with [Podman](https://podman.io/), [MongoDB](https://www.mongodb.com/) and [Python](https://www.python.org/).

Note : [CosmosDB Emulator](https://learn.microsoft.com/en-us/azure/cosmos-db/emulator) doesn't work with Docker/Opensuse ([Issues](https://github.com/Azure/azure-cosmos-db-emulator-docker/issues/84))

# Folders

```
├── data
|   ├── genere                  <--- Storage for generated files (by scripts_api)
├── scripts_api                 <--- Scripts to retrieve information from externe API
├── scripts_cosmodb             <--- Scripts to work with CosmosDB (Stopped because Azure CosmosDB Emulator not working correctly With Docker)
├── scripts_mongodb             <--- Scripts to work with MongoDB (Python)
```

# Tools

## MongoDB (Docker)

Command to manage the MongoDB environment :
- To load the Python MongoDB environment : `source mongodb_activate.sh`
- To init the MongoDB services : `./mongodb_init.sh`
- To start the MongoDB services : `./mongodb_start.sh`
- To stop the MongoDB services : `./mongodb_stop.sh`
- To clean all elements created with the MongoDB services : `./mongodb_clean.sh`
- To unload the Python MongoDB environment : `deactivate`

_Connexion with username/password : mongo/mongo_
