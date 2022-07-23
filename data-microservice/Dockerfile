FROM python:3
RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /home/app/data-microservice
COPY ./ /home/app/data-microservice
RUN pip install -r requirements.txt