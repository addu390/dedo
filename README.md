# DeDo for Secure Delivery (Work In Progress)

## The Problem 

<img src="./images/problem.png" width="60%">

## The Solution
<img src="./images/solution.png" width="60%">


## Installation

- Install `virtualenv` ([Reference](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/))

```
python3 -m pip install --user --upgrade pip
python3 -m pip --version
python3 -m pip install --user virtualenv
```

- Create a virtual environment and install dependencies

```
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

## Migrations

- Create database: `CREATE DATABASE dedo;`
- Run migrations:
```
python3 manage.py migrate admin
python3 manage.py migrate core
```

## Start Server

- Development Server: `python3 manage.py runserver`
