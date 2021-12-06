# flask-todo
## _simple boilerplate code for flask RESTful backend_

![Flask](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)
![Flask](https://miro.medium.com/max/876/1*0G5zu7CnXdMT9pGbYUTQLQ.png)

flask-todo is a simple python folder structure for REST APIs


## Features
- simple structure
- Easy to understand codebase
- integrated with MySQL using SQLAlchemy
- uses Makefile for project control

## Installation

flask-todo requires [Python](https://www.python.org/) to run.

Install the dependencies and devDependencies and start the server.

```sh
cd flask-todo
cp .env.example .env  #create .env file from .env.example file, change SQL database url
make setup
make run
```

For production environments...

 - change the value  of ``FLASK_ENV`` in .env file to 'production'
```sh
make run
```
