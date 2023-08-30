from django.shortcuts import render , redirect , HttpResponse
from .models import SiteInfo , About
from treatment.models import Treatment
from doctors.models import Doctors
from departements.models import Departements
from contact.forms import PostForm
from contact.models import Contact
from appointement.forms import AppointForm
# Create your views here.



def home(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    doctors = Doctors.objects.all()
    treatments = Treatment.objects.all()
    departemetns = Departements.objects.all()
    all_messages = Contact.objects.filter(activate=True).order_by('-id')[:10]
    contact_form = PostForm
    appoint_form = AppointForm
    title = "خانه"
    context = {
        "title" : title,
        "information" : information,
        "about" : about,
        "doctors" : doctors,
        "treatments" : treatments,
        "departemetns" : departemetns,
        "contact_form" : contact_form,
        "appoint_form" : appoint_form,
        "all_messages" : all_messages
    }
    return render(request , 'main/home.html' , context)





def about(request):
    information = SiteInfo.objects.last()
    about = About.objects.last()
    title = "درباره ما"
    context = {
        "title" : title,
        "information" : information,
        "about" : about,
    }
    return render(request , 'main/about.html' , context)

