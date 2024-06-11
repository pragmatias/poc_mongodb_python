#!/bin/sh

source ./utils.sh
source ./config_mongodb.sh

TIMEOUT=10
SLEEPING=10

# Stop the pod 
CONTAINER_RUNNING=$(podman ps -p -a --filter "pod=${POD_NAME}" --filter "name=${CONTAINER_NAME}" --filter "status=running" | wc -l)
if [ ${CONTAINER_RUNNING} -eq 2 ]
then
    print_log "Stopping CONTAINER [${CONTAINER_NAME}] ..."
    podman pod stop ${POD_NAME}
    print_log "Stopping CONTAINER [${CONTAINER_NAME}] OK!"
fi










