from django.urls import re_path, path

from migrainetracker.views import index, entry, register, login

urlpatterns = [
    path('entry', entry),
    path('register', register),
    path('login', login),
    re_path('', index),
]
