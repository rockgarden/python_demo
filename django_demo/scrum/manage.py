# hostname $ django-admin.py startproject scrum
# hostname $ cd scrum
# hostname $ python3 manage.py startapp board
# hostname $ python3 manage.py makemigrations board
# hostname $ python3 manage.py migrate
# hostname $ python3 manage.py createsuperuser
# $ python3 manage.py runserver



import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrum.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
