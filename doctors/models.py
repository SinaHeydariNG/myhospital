from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.





class Doctors(models.Model):
    name = models.CharField(max_length=225)
    lastname = models.CharField(max_length=225,null=True , blank=True)
    description = RichTextField()
    images = models.ImageField(upload_to = 'doctores/images/%y/%m/%d/')

