FROM python:3
RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /home/app/api-service
COPY ./ /home/app/api-service
RUN pip install -r requirements.txt