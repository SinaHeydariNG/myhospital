from django.shortcuts import render
from .models import Treatment
from main.models import SiteInfo , About
# Create your views here.
def list(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    treatments = Treatment.objects.all()
    title = "روش های درمانی"
    context = {
        "title" : title,
        "information" : information,
        "about" : about,
        "treatments" : treatments
    }
    return render(request , 'treatment/list.html' , context)