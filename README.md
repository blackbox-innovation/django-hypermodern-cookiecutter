django-hypermodern-cookiecutter
===============================

django-hypermodern-cookiecutter is a cookiecutter project designed to help you get started with building a Django application quickly. The project includes a variety of pre-built templates, views, and settings to help you build a scalable solution in no time. With our tested design and development process, you can convert unique ideas into reality.

Note
----

This project is currently tied to the `blackbox.ms` infrastructure, which uses a private GitLab server for deployment and local development on a Mac.

Work in Progress
----------------

Please note that this project is a work in progress and is not yet production-ready. We're actively developing it and making improvements, but it's not yet recommended for use in production environments.

Features
--------

-   Python 3.9
-   Python Poetry for dependency management
-   DjLint for code quality
-   React support via Django Compressor and ESBuild
-   Dependabot for automated dependency updates
-   A nicely styled django admin with [django-baton](https://github.com/otto-torino/django-baton)
-   Authentication using [django-allauth](https://github.com/pennersr/django-allauth)
-   Form rendering using [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) with Bootstrap 5

Using django-hypermodern-cookiecutter with Cookiecutter
-------------------------------------------------------

To use the django-hypermodern-cookiecutter with [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/), make sure you have Cookiecutter installed on your machine. Then run the following command:

`cookiecutter git@github.com:blackbox-ms/django-hypermodern-cookiecutter.git`

This will generate a new Django project in a directory named after the project you specified during the cookiecutter prompt. The directory will contain all of the files necessary to get started with your new Django project.

Testing
-------

To run the tests, make sure you have the dependencies installed and run the following command:

`pytest`

Contributing
------------

We welcome contributions to the django-hypermodern-cookiecutter project. To contribute, please fork this repository, make your changes, and create a pull request.

About Blackbox.ms and Blackbox Innovation
-----------------------------------------

[![Blackbox.ms](https://www.blackbox.ms/assets/img/large-logo-on-white.svg)](https://blackbox.ms) 

This is the website of Blackbox Innovation, a software development and digital consultancy company. We build innovative digital products with our proven design and development processes, turning unique ideas into reality.
