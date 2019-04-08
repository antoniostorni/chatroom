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

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd chatroom
    celery -A chatroom.taskapp worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.



App usage
^^^^^^

http://localhost:8000/admin/

Add chat rooms:
http://localhost:8000/admin/chat/room/

List messages
http://localhost:8000/messages/

Add messages
http://localhost:8000/messages/add/
