# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-client postgresql-dev zlib-dev jpeg-dev gcc geos proj gdal binutils python3-dev musl-dev

RUN apk add --no-cache \
        geos \
        proj \
        gdal \
        binutils \
    && ln -s /usr/lib/libproj.so.15 /usr/lib/libproj.so \
    && ln -s /usr/lib/libgdal.so.20 /usr/lib/libgdal.so \
    && ln -s /usr/lib/libgeos_c.so.1 /usr/lib/libgeos_c.so

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .