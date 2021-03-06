# DeDo for Secure Delivery
A sample project using Post GIS and Leaflet; blog post on [django-postgis](https://www.pyblog.xyz/django-postgis)

| The Problem | The Solution |
| -- | -- |
| <img src="./images/problem.png"> | <img src="./images/solution.png"> |

## Installation (Docker)

- Install Docker and run `docker-compose up`

- Run migrations: 

```
docker-compose exec web python3.9 manage.py makemigrations core
docker-compose exec web python3.9 manage.py migrate
```

- Create Super User: 

```
docker-compose exec web python3.9 manage.py createsuperuser
```


## Installation (Local Set-up)

- Install `virtualenv` ([Reference](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/))

```
python3 -m pip install --user --upgrade pip
python3 -m pip --version
python3 -m pip install --user virtualenv
```

- Install Prerequisites

```
brew install postgresql
brew install postgis
brew install gdal
brew install libgeoip
```

- Create a virtual environment and install dependencies

```
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

- Start PostgreSQL Server

```
docker run --name=postgis -d -e POSTGRES_USER=<database-username> -e POSTGRES_PASS=<database-password> -e POSTGRES_DBNAME=<database-name> -p 5432:5432 kartoza/postgis:14-3.2
```

- Run migrations:

Local machine set-up

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Docker set-up

```
docker-compose exec web python3.9 manage.py makemigrations core
docker-compose exec web python3.9 manage.py migrate
```

- Start Server
    - Create a new file `.env` at the root of the project with the contents of `.env.example` with the correct values.
    - Start Development Server: `python3 manage.py runserver`
  
<hr>

## Common Issues:

- Permission denied on Linux: `sudo chmod 666 /var/run/docker.sock`
- Install Git on remote server: `sudo yum install git`
- Hostname(s)
  - Local MySQL server: `host.docker.internal`
  - Docker MySQL server in same network: `db` 
