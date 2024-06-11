#!/bin/sh

source ./utils.sh
TIMEOUT=10
SLEEPING=10

# create pod if needed
POD_EXISTS=$(podman pod ps --filter "name=${POD_NAME}" | wc -l)
if [ ${POD_EXISTS} -ne 2 ]
then
    print_log "Creating POD [${POD_NAME}] ..."
    podman pod create --name ${POD_NAME} -p 8081:8081 -p 10250-10255:10250-10255
    print_log "Creating POD [${POD_NAME}] OK!"
fi

# Create container if needed
CONTAINER_EXISTS=$(podman pod ps -p -a --filter "pod=${POD_NAME}" --filter "name=${CONTAINER_NAME}" | wc -l)
if [ ${CONTAINER_EXISTS} -ne 2 ]
then
    print_log "Creating CONTAINER [${CONTAINER_NAME}] ..."
    podman run -dt --pod ${POD_NAME} --name ${CONTAINER_NAME} mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest
    print_log "Creating CONTAINER [${CONTAINER_NAME}] OK!"
fi


# Check if container is OK
Reason: Host Extension RTL_ASSERT (0x00000003)

# Get the cert 
CONTAINER_UP=$()

curl -k -s https://localhost:8081/_explorer/emulator.pem > ${CONTAINER_NAME}.crt


# Stop the pod 
CONTAINER_RUNNING=$(podman pod ps -p -a --filter "pod=${POD_NAME}" --filter "name=${CONTAINER_NAME}" --filter "status=running" | wc -l)
if [ ${CONTAINER_RUNNING} -eq 2 ]
then
    print_log "Stopping CONTAINER [${CONTAINER_NAME}] ..."
    podman pod stop ${POD_NAME}
    print_log "Stopping CONTAINER [${CONTAINER_NAME}] OK!"
fi










