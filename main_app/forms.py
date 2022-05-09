from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Location

class Profile_Delete_Form(ModelForm):
    class Meta:
        model = User
        fields=[]

class Location_Update_Form(ModelForm):
    class Meta:
        model = Location
        fields='__all__'