# Sensor Data
This is a project of mine for learning FastAPI and Vue.js. Right now the functionality is limited as the web app shows two plots - temperature and humidity data from my RaspberryPi. However the project is well structured and can be easily extended. It is also very easy to set up as everything is deployed in docker containers so a `docker-compose up --build` followed by the database initializations should get you going. If I have time I will improve the web application, especially the frontend, implement a login page, add range filters etc. I am also open for interesting ideas.

## Tech stack
tl;dr:
* Frontend - [Vue.js](https://vuejs.org/)
* Backend - Python [FastAPI](https://fastapi.tiangolo.com/)
* Database - [PostgreSQL](https://www.postgresql.org/)
* ORM - [SQLAlchemy](https://www.sqlalchemy.org/) with [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* Deployment - Docker, Traefik, nginx

The backend is written in Python using the framework [FastAPI](https://github.com/tiangolo/fastapi). FastAPI is great at it allows for asynchronous functions and automatically generates an API documentation in the OpenAPI specification for you. The database in use is PostgreSQL with SQLAlchemy as the ORM and Alembic for database migrations. In the future I will perhaps try out InfluxDB which was developed with a focus on dealing with time series data. The frontend is written in Vue.js.

## Environments
There are three environments you can choose from:
1) Production environment in docker containers
2) Development environment in docker containers
3) Development environment without docker containers

### Production 

## Tech stack


Playing around with FastAPI

## Development environment with docker
```
docker-compose exec web alembic stamp head
docker-compose exec web alembic upgrade head
```
Create .env files

# Docker and docker-compose on Ubuntu
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04