#!/bin/bash
set -o errexit

python -m pip install --upgrade pip
# Install dependencies, collect static, migrate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
