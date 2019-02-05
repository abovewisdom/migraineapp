from django.urls import re_path, path

from migrainetracker.views import index, entry

urlpatterns = [
    path('entry', entry),
    re_path('', index),
]
