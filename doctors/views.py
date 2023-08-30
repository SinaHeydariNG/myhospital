from django.shortcuts import render
from main.models import SiteInfo , About
from .models import Doctors
# Create your views here.
def list(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    doctors = Doctors.objects.all()
    title = "دکتر ها"
    context = {
        "title" : title,
        "information" : information,
        "about" : about,
        "doctors" : doctors
    }
    return render(request , 'doctors/list.html' , context)

