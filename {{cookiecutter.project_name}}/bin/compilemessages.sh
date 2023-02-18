set -e

./manage.py make_messages --all --ignore .venv
./manage.py makemessages_djangojs --locale=de --domain djangojs --ignore=.venv --ignore=node_modules --ignore=static_root --ignore=vendor --language Python --extension tsx
django-admin compilemessages --ignore=.venv
