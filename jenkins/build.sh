#!/bin/bash

docker build -t screamzle/workoutapp:latest .
docker tag screamzle/workoutapp:latest screamzle/workoutapp:$BUILD_NUMBER
docker build -t screamzle/sqldbimage db/.
docker tag screamzle/sqldbimage:latest screamzle/sqldbimage:$BUILD_NUMBER