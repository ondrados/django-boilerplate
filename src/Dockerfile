# pull official base image
FROM python:3.9-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src

RUN apt-get update \
    && apt -y install build-essential \
    && apt-get -y install python3-dev libpq-dev netcat libmagic-dev \
    && pip install --upgrade pip \
    && pip install psycopg2

# copy requirements
COPY ./requirements.txt /usr/src/

# install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# copy project
COPY . /usr/src/

# run server
CMD ["/usr/src/start.sh"]
