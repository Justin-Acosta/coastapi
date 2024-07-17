#!/bin/bash

rm db.sqlite3
rm -rf ./coastapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations coastapi
python3 manage.py migrate coastapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

