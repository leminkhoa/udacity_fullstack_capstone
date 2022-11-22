# Money App Backend

## Getting Started

### Installing Dependencies

#### Python 3.9

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the servers

From within the `./backend` directory first ensure you are working using your created virtual environment.

### Postgresql Server
Before starting Flask app, make sure Postgresql server is on:
- Start Postgresql server locally: `sudo service postgresql start`
- Run script `./setup_db.sh budget_db`


### Flask Server

To run the server, execute:

```bash
FLASK_APP=money_app flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Running test

To ensure all apis work properly, this repository use `pytest` to test all queries in a test database. To run test, follow steps as below:
- Start a Postgresql server locally: `sudo service postgresql start`
- Run script `./run_test.sh`


## Call API From Postman
Once Flask app is running, we can test API from local using **Postman**. 

Import [Postman collection](./postman/Udacity_Capstone_Fullstack.postman_collection.json) into Postman for loading pre-defined collections.

There are 2 environments to run:
- Local: To call api from local database. Import environment [here](./postman/Udacity%20Money%20App%20Environment%20-%20Local.postman_environment.json)
- Remote - **Heroku**: To call api from Heroku App. Import environment [here](./postman/Udacity%20Money%20App%20Environment%20-%20Heroku.postman_environment.json)

### API Documentations

For detailed API Documentations, please check folder [api_docs](./api_docs)
