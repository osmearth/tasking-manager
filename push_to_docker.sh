#!/bin/sh
docker-compose build tm
docker-compose up -d tm
docker commit taskingmanager_tm_1 quay.io/loggingroads/tm3
docker push quay.io/loggingroads/tm3
