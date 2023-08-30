from django.urls import  path
from . import views

app_name = 'contact'

urlpatterns = [
    path('submit/' , views.submit_message , name='submit'),
    path('add/' , views.add , name='add'),
]