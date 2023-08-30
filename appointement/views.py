from django.shortcuts import render , redirect , HttpResponse
from .forms import AppointForm
from .models import Appointements
from django.contrib import messages
# Create your views here.
def submit_appointement(request):
    if request.method == "POST":
        my_form = AppointForm(request.POST)
        if my_form.is_valid():
            new_meesage = Appointements.objects.create(
                name = my_form.cleaned_data['name'],
                date = my_form.cleaned_data['date'],
                phone = my_form.cleaned_data['phone'],
                symptoms = my_form.cleaned_data['symptoms'],
                departements = my_form.cleaned_data['departements'],
                doctors = my_form.cleaned_data['doctors'],
            )
            new_meesage.save()
            messages.success(request,"پیام شما با موفقیت ارسال شد!")
            return redirect("main:home")
        else:
            messages.error(request,"مشکلی در ارسال پیام پیش آمد")
            return redirect("main:home")
    else:
        messages.info(request,"مشکلی در ارسال درخواست شما پیش آمد")
        return redirect("main:home")