from django.urls import re_path, path
from web.views import index, entry, register, userlogin, userlogout, table, dashboard

urlpatterns = [
    path('', index),
    path('entry', entry),
    path('register', register),
    path('userlogin', userlogin),
    path('userlogout', userlogout),
    re_path('dashboard', table.as_view(template_name ="dashboard.html"))
]
