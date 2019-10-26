#!/bin/bash

cid=`docker run -itd --privileged saintube/kind:v1.14.4`
docker ps
docker exec -i $cid cat /etc/hosts
