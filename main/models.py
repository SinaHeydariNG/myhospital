from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class SiteInfo(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    copyright = models.CharField(max_length=225 , null=True , blank=True)



class About(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    copyright = models.CharField(max_length=225)
    description = RichTextField()