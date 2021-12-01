from django import forms
from AppTwo.models import User_details

class NewUserForm(forms.ModelForm):
    class Meta:
        model=User_details
        fields="__all__"
