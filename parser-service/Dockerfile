FROM python:3
RUN apt-get update -y && apt-get install -y build-essential
WORKDIR /home/app/parser-service
COPY ./ /home/app/parser-service
RUN pip install -r requirements.txt