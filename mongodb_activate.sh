#!/bin/sh

source ./utils.sh
source ./config_mongodb.sh


# check if python env exist
if [ ! -d ".${PYTHON_ENV_NAME}" ]
then 
  print_log "Creating the folder .${PYTHON_ENV_NAME} ..."
  python3 -m venv --prompt ${PYTHON_ENV_NAME} .${PYTHON_ENV_NAME}
  print_log "Folder .${PYTHON_ENV_NAME} OK !"
fi

print_log "Source the environment ..."
source .${PYTHON_ENV_NAME}/bin/activate
print_log "Environment OK !"



# Install python environment libraries (local)
LIBS_INSTALLED=$(pip list | grep -E "pymongo|requests" | wc -l)

if [ ${LIBS_INSTALLED} -ne 2 ]
then
  print_log "Install requirements ..."
  pip install -U pymongo requests
  print_log "Requirements OK !"
fi




