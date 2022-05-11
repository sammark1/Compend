from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Location

MODEL_CHOICES = (
    ('NPC', 'NPC'),
    ('Location', 'Location'),
)

class UploadFileForm(forms.Form):
    title = forms.CharField(label="title", max_length=50)
    data_type = forms.CharField(label="Select a model", max_length=32, widget=forms.Select(choices=MODEL_CHOICES))
    file = forms.FileField()

class Profile_Delete_Form(ModelForm):
    class Meta:
        model = User
        fields=[]

# class Location_Update_Form(ModelForm):
#     class Meta:
#         model = Location
#         fields='__all__'