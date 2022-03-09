#!/bin/bash

if docker inspect  sqldb_container > /dev/null 2>&1 ; then docker stop sqldb_container; docker rm sqldb_container; fi
docker run -d --network my-network --name sqldb_container screamzle/sqldbimage
sleep 10
if docker inspect  workoutapp_container > /dev/null 2>&1 ; then docker stop workoutapp_container; docker rm workoutapp_container; fi
docker run -d --network my-network --name workoutapp_container screamzle/workoutapp
if docker inspect  nginx_container > /dev/null 2>&1 ; then docker stop nginx_container; docker rm nginx_container; fi
docker run -d --network my-network --name nginx_container -p 80:80 --mount type=bind,src=$WORKSPACE/nginx/nginx.conf,dst=/etc/nginx/nginx.conf nginx