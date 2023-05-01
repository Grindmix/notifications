FROM python:3.8.13-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        libffi-dev \
                        musl-dev \
                        postgresql-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]