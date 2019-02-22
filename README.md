# Employee Directory Flask App
An employee directory app created using Python Flask and MySQL Employees sample database.
The Employees database is available from [Employees DB on GitHub](https://github.com/datacharmer/test_db). You can download a prepackaged archive of the data, or access the information through Git.

## Quickstart
This project is managed using Pipenv. 

Install pipenv:
```
$ pip install --user pipenv
```
Clone / create project repository:
```
$ cd <projectfolder>
```

Install packages from Pipfile:
```
$ pipenv install
```
Activate the Pipenv shell:
```
$ pipenv shell
```

Set the environment variable and run the app:
```
$ export FLASK_APP=empdir
$ flask run
 * Running on http://127.0.0.1:5000/
```
