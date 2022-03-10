# Use mysql 8.0
FROM mysql:8.0
# Add a database and root password
ENV MYSQL_DATABASE=workoutdb
ENV MYSQL_USER=matt
ENV MYSQL_PASSWORD=root
ENV MYSQL_ROOT_PASSWORD=root
# add volume
VOLUME workout_volume:/var/lib/mysql
# create schema if necessary
WORKDIR DevOps-Project/db
COPY schema.sql /docker-entrypoint-initdb.d/