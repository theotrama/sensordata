# Sensor Data
This is a project of mine for learning FastAPI and Vue.js. For a live demo go to [http://159.89.239.100/](http://159.89.239.100/) where the web app is running. You can find the API documentation at [http://159.89.239.100/docs](http://159.89.239.100/docs). Right now the functionality is limited as the web app shows two plots - temperature and humidity data from my RaspberryPi. However the project is well structured and easily extendable. It is also very easy to set up as everything is deployed in docker containers so a `docker-compose up --build` followed by the database initializations should get you going. If I have time I will improve the web application, especially the frontend, implement a login page, add range filters etc. I am also open for interesting ideas.

## Tech stack
* Frontend - [Vue.js](https://vuejs.org/)
* Backend - Python [FastAPI](https://fastapi.tiangolo.com/)
* Database - [PostgreSQL](https://www.postgresql.org/)
* ORM - [SQLAlchemy](https://www.sqlalchemy.org/) with [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* Deployment - Docker, Traefik, nginx

The backend is written in Python using the framework [FastAPI](https://github.com/tiangolo/fastapi). FastAPI is great at it allows for asynchronous functions and automatically generates an API documentation in the OpenAPI specification for you. The database in use is PostgreSQL with SQLAlchemy as the ORM and Alembic for database migrations. In the future I will perhaps try out InfluxDB which was developed with a focus on dealing with time series data. The frontend is written in Vue.js.

## Environments
There are three environments you can choose from:
* Production environment in docker containers
* Development environment in docker containers
* Development environment without docker containers


### Production environment in docker containers
The production environment uses gunicorn as the application server and traefik as the reverse proxy. Deploy the production environment to your server and go to the projects root directory. Before spinning up the docker containers, you have to edit the `backend/.env.prod.db-sample` file. Copy the file and edit the environment variables in `backend/.env.prod.db`
```
cp backend/.env.prod.db-sample backend/.env.prod.db
vim backend/.env.prod.db
```

Then you can start the containers and run the initial database migrations. 
```
docker-compose -f docker-compose.prod.yml up --build
docker-compose -f docker-compose.prod.yml exec web alembic upgrade head
```

The web app should now be available on your server. Go to [http://<SERVER_IP>/docs](http://<SERVER_IP>/docs) for the API documentation.

Access the logs with `docker-compose -f docker-compose.prod.yml logs`

### Development environment in docker containers
The production environment uses gunicorn as the application server and traefik as the reverse proxy. Deploy the production environment to your server and go to the projects root directory. Before spinning up the docker containers, you have to edit the `backend/.env.dev.db-sample` file. Copy the file and edit the environment variables in `backend/.env.dev.db`
```
cp backend/.env.dev.db-sample backend/.env.dev.db
vim backend/.env.dev.db
```

Then you can start the containers and run the initial database migrations. 
```
docker-compose up --build
docker-compose exec web alembic upgrade head
```

The web app should now be available on your server. Go to [http://<SERVER_IP>/docs](http://<SERVER_IP>/docs) for the API documentation.

Access the logs with `docker-compose logs`

### Development environment without docker containers
As the backend and frontend are decoupled you have to start both of them manually.

#### Backend
Use the `requirements.txt` file to create a virtual environment.

On macOS and Linux:
```
cd backend/src/
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

On Windows:
```
cd backend/src/
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```

Make the initial database migrations and start the development server.
```
cd backend/src/
alembic upgrade head
uvicorn app.main:app --reload
```

#### Frontend
Switch to the frontend directory and simply run the development server.
```
cd fronted/
npm run server
```

## Todo
- [ ] Test cases
- [ ] Login
- [ ] Better UI with more functions
- [ ] CI
- [x] Load passwords from env file
- [ ] Buy domain and setup Let's Encrypt certificate