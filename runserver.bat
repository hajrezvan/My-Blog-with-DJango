@echo off
title runserver
start cmd /k "D: && cd D:\Programming\Python\Blog\Scripts && activate && cd .. && python manage.py runserver && python manage.py makemigrations && python manage.py migrate"