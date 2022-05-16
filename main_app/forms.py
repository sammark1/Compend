from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Location, NPC

MODEL_CHOICES = (
    ('NPC', 'NPC'),
    ('Location', 'Location'),
)

class Upload_File_Form(forms.Form):
    data_type = forms.CharField(label="Select a model", max_length=32, widget=forms.Select(choices=MODEL_CHOICES))
    file = forms.FileField()

class Profile_Delete_Form(ModelForm):
    class Meta:
        model = User
        fields=[]

class Location_Upload_Form(ModelForm):
    class Meta:
        model = Location
        fields=['name', 'campaign', 'location_type', 'description']

class NPC_Upload_Form(ModelForm):
    class Meta:
        model = NPC
        fields=[
            'given_name',
            'family_name',
            'campaign',
            'alignment',
            'pronoun',
            'npc_class',
            'npc_race',
            'age',
            'physical',
            'profession',
        ]