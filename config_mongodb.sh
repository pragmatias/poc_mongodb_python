#!/bin/sh

print_log "Export variable ..."
export PYTHON_ENV_NAME="venv_mongodb"
export POD_NAME="mongo-pod"
export CONTAINER_NAME="${POD_NAME}-db"
export CONTAINER_USER="mongo"
export CONTAINER_PASS="mongo"
print_log "Export variable OK !"