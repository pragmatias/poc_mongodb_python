import pathlib
from azure.cosmos import CosmosClient, SSLConfiguration

dir_root  = pathlib.Path(__file__).parent.parent.resolve()
dir_data_json = f"{dir_root}/data/json"

certif = f"{dir_root}/docker/emulatorcert.crt"
config_ssl = SSLConfiguration()
config_ssl.SSLCaCerts = certif

config_connect = {
    "ssl" : config_ssl,
    "url" : "https://localhost:8081",
    "credential" : (
        "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGG"
        "yPMbIZnqyMsEcaGQy67XIw/Jw=="
    )
}

def getCosmosClient(config=config_connect) :
    return CosmosClient(
        url=config["url"],
        ssl_config=config["ssl"],
        credential=config["credential"],
        )

