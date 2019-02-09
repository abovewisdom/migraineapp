from django.urls import re_path, path

from web.views import index, entry, register, login

urlpatterns = [
    path('entry', entry),
    path('register', register),
    path('login', login),
    re_path('', index),
]
