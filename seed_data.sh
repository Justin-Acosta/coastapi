#!/bin/bash

rm db.sqlite3
rm -rf ./coastapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations coastapi
python3 manage.py migrate coastapi
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata players
python manage.py loaddata locations
python manage.py loaddata fishtypes
python manage.py loaddata fish
python manage.py loaddata baits


