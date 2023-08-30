from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.





class Departements(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225,null=True , blank=True)
    description = RichTextField()
    images = models.ImageField(upload_to = 'treatments/images/%y/%m/%d/')

