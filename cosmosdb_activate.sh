#!/bin/sh

source ./utils.sh

print_log "Export variable ..."
export PYTHON_ENV_NAME="venv_cosmosdb"
export POD_NAME="cosmos-pod"
export CONTAINER_NAME="${POD_NAME}-db"
print_log "Export variable OK !"

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
LIBS_INSTALLED=$(pip list | grep -E "azure-cosmos" | wc -l)

if [ ${LIBS_INSTALLED} -ne 1 ]
then
  print_log "Install requirements ..."
  pip install -U azure-cosmos
  print_log "Requirements OK !"
fi




