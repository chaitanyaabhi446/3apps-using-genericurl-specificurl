from django.urls import path
from uspolo.views import*
app_name='what'
urlpatterns=[
    path('tshirts/',tshirts,name='tshirts'),
]