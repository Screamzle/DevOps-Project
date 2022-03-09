#Use Python 3.8.10 as a base image
FROM python:3.8.10
# Copy contents into image
WORKDIR /DevOps-Project
COPY . .
# Set environment variables
ENV FLASK_ENV=development
ENV FLASK_APP=application
ENV FLASK_RUN_HOST=0.0.0.0
ENV DATABASE_URI=mysql+pymysql://matt:root@root@meh-jenkins-server.uksouth.cloudapp.azure.com:3306/workoutdb
# install pip dependencies from requirements file
RUN pip3 install -r requirements.txt
# Expose correct port
EXPOSE 5000
# Create an entrypoint
CMD ["flask", "run"]