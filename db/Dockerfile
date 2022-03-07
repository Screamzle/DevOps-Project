# Use mysql 8.0 as the flask-app is not set up to work with later versions
FROM mysql:8.0
# Add a database and root password
ENV MYSQL_DATABASE=workoutdb
ENV MYSQL_ROOT_PASSWORD=root
# add volume
VOLUME workout_volume:/var/lib/mysql