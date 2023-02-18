# Python build stage
FROM nikolaik/python-nodejs:python3.9-nodejs14-bullseye

# set timezone to berlin
ENV TZ=Europe/Berlin
# set python path for django admin command
ENV PYTHONPATH=/home/pn

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get install -y tzdata && \
    dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update \
    #   # dependencies for building Python packages
    #   && apt-get install -y build-essential \
    #   # psycopg2 dependencies
    #   && apt-get install -y libpq-dev \
    #   # pillow dependencies
    #   && apt-get install -y libjpeg-dev zlib1g-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    # postgres for pg_isready
    && apt-get install -y postgresql-client \
    #   # weasyprint dependencies
    #   && apt-get install -y libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# DART SASS
ADD https://github.com/sass/dart-sass/releases/download/1.52.3/dart-sass-1.52.3-linux-x64.tar.gz /tmp/dart-sass.tar.gz
RUN tar -C /opt/ -xzvf /tmp/dart-sass.tar.gz && \
    ln -s /opt/dart-sass/sass /usr/local/bin/sass

WORKDIR /home/pn

COPY --chown=pn:pn ./deployment/django/cmds/* /home/pn/cmds/
RUN sed -i 's/\r$//g' /home/pn/cmds/*
RUN chmod -R +x /home/pn/cmds

COPY --chown=pn:pn poetry.lock pyproject.toml poetry.toml ./

# switch to user, from now on we do everything as pn
USER pn

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-dev

# Frontend deps
COPY package.json yarn.lock ./

RUN yarn --frozen-lockfile

# Run the application from the "app" directory and as the "django" user
COPY --chown=pn:pn . /home/pn

# Call collectstatic and compress (customize the following line with the minimal environment variables needed for manage.py to run):
RUN poetry run python manage.py collectstatic --noinput --settings={{cookiecutter.project_name}}.settings.base --ignore "scss" --ignore "CACHE"
# call django-comporessor for offline compression
RUN poetry run python manage.py compress --settings={{cookiecutter.project_name}}.settings.base  --force

# compile languages
RUN poetry run django-admin compilemessages --settings={{cookiecutter.project_name}}.settings.base --ignore=.venv --ignore=virtualenvs