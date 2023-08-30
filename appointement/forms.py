from django import forms
from .models import Appointements


class AppointForm(forms.ModelForm):



    class Meta:
        model = Appointements
        fields = ('name' , 'date' , 'phone' , 'symptoms' , 'departements' , 'doctors')

    def __init__(self, *args, **kwargs):
        super(AppointForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "نام"
        self.fields['date'].label = "تاریخ"
        self.fields['phone'].label = "شماره تلفن"
        self.fields['symptoms'].label = "نشانه ها"
        self.fields['departements'].label = "سازمان"
        self.fields['doctors'].label = "دکتر ها"