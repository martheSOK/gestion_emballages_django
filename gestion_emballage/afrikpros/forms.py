from django import forms
from .models import *
from django.contrib.auth.models import User



class DepotForm(forms.ModelForm):
    pass
    class Meta:
        model=Depot
        fields='__all__'