from django.urls import re_path, path

from web.views import index, entry, register, login, userlogout

urlpatterns = [
    path('entry', entry),
    path('register', register),
    path('login', login),
    path('userlogout', userlogout),
    re_path('', index),
]
