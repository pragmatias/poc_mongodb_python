#!/bin/sh

source ./utils.sh
TIMEOUT=10
SLEEPING=10

# Stop the pod 
CONTAINER_RUNNING=$(podman pod ps -p -a --filter "pod=${POD_NAME}" --filter "name=${CONTAINER_NAME}" --filter "status=stopped" | wc -l)
if [ ${CONTAINER_RUNNING} -eq 2 ]
then
    print_log "Starting CONTAINER [${CONTAINER_NAME}] ..."
    podman pod start ${POD_NAME}
    print_log "Starting CONTAINER [${CONTAINER_NAME}] OK!"
fi










