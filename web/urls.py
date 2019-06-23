from django.urls import re_path, path
from web.views import index, entry, register, userlogin, userlogout, MigraineListTable, dashboard, tour, whytrack

urlpatterns = [
    path('', index),
    path('entry', entry),
    path('register', register),
    path('userlogin', userlogin),
    path('userlogout', userlogout),
    path('tour', tour),
    path('whytrack', whytrack),
    re_path('dashboard', MigraineListTable.as_view(template_name ="dashboard.html"))
]

