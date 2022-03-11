# Use mysql 8.0
FROM mysql:8.0
# Add a database and root password
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
# add volume
VOLUME workout_volume:/var/lib/mysql
# create schema if necessary
WORKDIR DevOps-Project/db
COPY schema.sql /docker-entrypoint-initdb.d/