from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur


ROLE = (
        ('admin', 'Admin'),
        ('client', 'Client'),
        ('freelancer','Freelancer'),
    )
    
class SignUpForm(UserCreationForm):

    phone_number=forms.CharField(max_length=10,required=False,label="Phone Number")
    role =forms.ChoiceField(choices = ROLE, label="", initial='', widget=forms.Select(), required=True)


    class Meta:
        model = Utilisateur
        fields = ('first_name', 'last_name', 'username', 'email','phone_number', 'password1', 'password2', 'role')