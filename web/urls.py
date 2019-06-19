from django.urls import re_path, path
from web.views import index, entry, register, userlogin, userlogout, table, dashboard, tour

urlpatterns = [
    path('', index),
    path('entry', entry),
    path('register', register),
    path('userlogin', userlogin),
    path('userlogout', userlogout),
    path('tour', tour),
    path('whytrack', whytrack),
    re_path('dashboard', table.as_view(template_name ="dashboard.html"))
]
