# base image
FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# set up Nginx
RUN apt-get update && apt-get install -y nginx
RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/sites-enabled/

# start Nginx and run Django
CMD service nginx start && python manage.py runserver 0.0.0.0:8000
