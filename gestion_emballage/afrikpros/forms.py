from django import forms
from .models import *
from django.contrib.auth.models import User



class DepotForm(forms.ModelForm):
    pass
    class Meta:
        model=Depot
        fields='__all__'



class FournisseurForm(forms.ModelForm):
    pass
    class Meta:
        model=Fournisseur
        fields='__all__'

class UserForm(forms.ModelForm):
    pass
    class Meta:
        model=Personne
        fields='__all__'
