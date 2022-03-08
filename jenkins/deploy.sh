#!/bin/bash

if docker inspect  workoutapp_container > /dev/null 2>&1 ; then docker stop workoutapp_container; docker rm workoutapp_container; fi
docker run -d --network my-network --name workoutapp_container screamzle/workoutapp
if docker inspect  sqldbimage_container > /dev/null 2>&1 ; then docker stop sqldbimage; docker rm sqldbimage_container; fi
docker run -d --network my-network --name sqldbimage_container screamzle/sqldbimage
if docker inspect  nginx_container > /dev/null 2>&1 ; then docker stop nginx_container; docker rm nginx_container; fi
docker run -d --network my-network --name nginx -p 80:80 --mount type=bind,src=$WORKSPACE/nginx/nginx.conf,dst=/etc/nginx/nginx.conf nginx