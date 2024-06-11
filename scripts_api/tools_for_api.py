import json 
import pathlib
import os
from datetime import datetime as dt


dir_root  = pathlib.Path(__file__).parent.parent.resolve()
dir_gen = f"{dir_root}/data/genere"

type_log_inf = "INF"
type_log_warn = "WRN"
type_log_err = "ERR"

def __get_dir(dir,folder):
    if (folder != ""):
        res_dir = dir+"/"+folder
        if not(os.path.exists(res_dir)):
            os.makedirs(name=res_dir,exist_ok=True)
        return res_dir
    else:
        raise Exception("Folder","empty")

def get_gen_dir(folder):
    return __get_dir(dir_gen,folder)



def print_log(message,type=type_log_inf):
    date_str = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{date_str} - {type} - {message}")



if __name__ == "__main__":   
    pass