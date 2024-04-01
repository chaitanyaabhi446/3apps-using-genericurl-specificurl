from django.urls import path
from gap.views import* 
app_name='some'
urlpatterns=[
    path('hoddies/',hoddies,name='hoddies'),
]