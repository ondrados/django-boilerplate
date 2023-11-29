# pull official base image
FROM python:3.11-alpine as base

# set work directory
WORKDIR /usr/src

# install build dependencies
RUN apk add --update --virtual .build-deps \
    build-base \
    python3-dev \
    libpq-dev \
    libffi-dev

# install python dependencies
COPY ./requirements.txt /usr/src/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf requirements.txt


FROM python:3.11-alpine as runtime

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src

# install runtime dependencies
RUN apk add libpq netcat-openbsd

# copy installed python packages
COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

# create a non-root user 'app_user'
RUN adduser -DH app_user

# copy project
COPY . /usr/src/

# change ownership of project files to app_user
RUN chown -R app_user:app_user /usr/src/

# switch to the 'app_user'
USER app_user

# run server
CMD ["/usr/src/start.sh"]
