Switch (cd) to fab_airflow

```bash
$ pip install -r requirements.txt
```

```python
$ flask fab create-app
Your new app name: first_app
Your engine type, SQLAlchemy or MongoEngine [SQLAlchemy]:
Downloaded the skeleton app, good coding!
$ cd first_app
# Use export if you are on Linux
$ set FLASK_APP=app 
$ flask fab create-admin
    Username [admin]:
    User first name [admin]:
    User last name [user]:
    Email [admin@fab.org]:
    Password:
    Repeat for confirmation:
$ flask run
```