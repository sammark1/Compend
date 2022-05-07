from django.forms import ModelForm
from django.contrib.auth.models import User

class Profile_Delete_Form(ModelForm):
    class Meta:
        model = User
        fields=[]