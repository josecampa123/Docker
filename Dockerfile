#Version de python
FROM python:3.9

#variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#la carpeta con la que trabajamos
WORKDIR /code
#intale las dependencias

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#copia el proyecto
COPY . /code/
