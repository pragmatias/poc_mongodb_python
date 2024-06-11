import pathlib
import os
import datetime
from pymongo import MongoClient

dir_root  = pathlib.Path(__file__).parent.parent.resolve()


config_connect = {
    "user" : os.environ.get("CONTAINER_USER","mongo"),
    "pass" : os.environ.get("CONTAINER_PASS","mongo"),
    "cluster" : "localhost",
    "port" : "27017"
}


def getMongoClient():
   url_connect = f"mongodb://{config_connect['user']}:{config_connect['pass']}" \
                            + f"@{config_connect['cluster']}:{config_connect['port']}/"
   return MongoClient(url_connect)



def printLog(message : str):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_date} - {message}")

if __name__ == "__main__":   
    pass