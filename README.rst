chatroom
========

Chat app
The main structure of this app was made with django-cookicutter
https://github.com/pydanny/cookiecutter-django

:License: GPLv3


Basic Commands
--------------

The easiest way to run the project is with docker-compose

docker-compose -f local.yml build


docker-compose -f local.yml run --rm django python manage.py makemigrations

docker-compose -f local.yml run --rm django python manage.py migrate

docker-compose -f local.yml run --rm django python manage.py createsuperuser

docker-compose -f local.yml up


Celery
^^^^^^

This app comes with Celery and Redis.

To run a celery worker:

.. code-block:: bash

    cd chatroom
    celery -A chatroom.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.


App usage
^^^^^^

It's convenient to create a superuser to test first.

http://localhost:8000/

New users can be created, but the email backend is not configured on the
development environment.

You can enable a user by checking the console messages, look at the confirmation URL
and open it on a browser.

You can use the app with the top bar navigation menu.
