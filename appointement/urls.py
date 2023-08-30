from django.urls import  path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('submit/' , views.submit_appointement , name='submit'),
]