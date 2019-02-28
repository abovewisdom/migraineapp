from django.urls import re_path, path

from web.views import index, entry, register, userlogin, userlogout

urlpatterns = [
    path('entry', entry),
    path('register', register),
    path('userlogin', userlogin),
    path('userlogout', userlogout),
    re_path('', index),
]
