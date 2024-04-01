from django.urls import path
from allensolly.views import *
app_name='emo'
urlpatterns=[
    path('allensolly/',allensolly,name='allensolly'),
]