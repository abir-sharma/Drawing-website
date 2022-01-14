# forms.py
from django import forms
from .models import Artistss
  
class ArtistssForm(forms.ModelForm):
  
    class Meta:
        model = Artistss
        fields = '__all__'
     
  