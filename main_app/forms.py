from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Location

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class Profile_Delete_Form(ModelForm):
    class Meta:
        model = User
        fields=[]

# class Location_Update_Form(ModelForm):
#     class Meta:
#         model = Location
#         fields='__all__'