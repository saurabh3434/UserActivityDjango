# UserActivityDjango
This Project Contains models User and ActivityPeriod.

Prequisites:
Python3 and pip need to be installed.

# create Virtual Environment:
pip install vertualenv
virtualenv virtualenv_name

- to activate venv in linux:
source virtualenv_name/bin/activate

- to activate in windows:
virtualenv_name\Scripts\activate


#install requiremnts.txt
pip install -r env_setup/requirements.txt

- Dummy data is in activity/fixtures/dummy_data.yaml. 
for demo purpose using sqlite3, if want to use db, then need to update settings.py and do makemigration and migrate.
python manage.py makemigrations
python manage.py migrate

Before running server, run this command,
python manage.py loaddata dummy_data.yaml

Now run server:
python manage.py runserver 0.0.0.0:8000

GET Api: 
http://localhost:8000/users
