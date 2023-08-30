from django.urls import  path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('list/' , views.list , name='list'),
]