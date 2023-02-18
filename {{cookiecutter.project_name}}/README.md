# {{cookiecutter.project_name}}

# How to run on blackbox infrastructure

1. run `cookiecutter django-hypermodern-cookiecutter` to create a new project from the template
2. run `direnv allow`
3. run `createdb {{cookiecutter.project_name}}_dev`
4. run `poetry install && yarn`
5. run `poetry shell`
6. run `poetry run python manage.py migrate`
7. run `./manage.py runserver 0.0.0.0:8000`
   

## Deployment

1. create new gitlab project: `https://git.blackbox.ms/projects/new#blank_project`
2. create dns entry at `https://account.hexonet.net/#/dnszones/manage/blackbox.ms.`
3. fill out values in `roles/django_apps/vars` in blackbox-infrastructure and run `./execute-playbook prod --tags "django_apps_role"` there 
4. git add, commit and push


## Python poetry for depedency management

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

See https://python-poetry.org/docs/ for more info


