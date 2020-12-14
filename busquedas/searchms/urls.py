from django.conf.urls import url, include

from .views import *

urlpatterns =[
    url(r'^busqueda/(?P<buscado>\w+)/$', busqueda),

]