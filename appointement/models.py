from django.db import models
from departements.models import Departements
from doctors.models import Doctors
from django.utils import timezone
# Create your models here.


class Appointements(models.Model):
    name = models.CharField(max_length=225)
    date = models.DateTimeField(default = timezone.now())
    phone = models.CharField(max_length=225)
    symptoms = models.CharField(max_length=225)
    departements = models.CharField(max_length=225)
    doctors = models.CharField(max_length=225)