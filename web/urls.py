from django.urls import re_path, path
from web.views import index, entry, register, userlogin, userlogout, table

urlpatterns = [
    path('entry', entry),
    path('register', register),
    path('userlogin', userlogin),
    path('userlogout', userlogout),
    re_path('', table.as_view(template_name ="index.html")),
]
