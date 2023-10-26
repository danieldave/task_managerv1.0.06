from django import forms
from django.contrib.auth.forms import UserCreationForm
#rom django.contrib.auth.models import User
from .models import CustomUser



class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=254)
    home_address = forms.CharField(max_length=100)
    profile_picture = forms.ImageField(required=False)
    office = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'phone_number', 'email', 'home_address', 'profile_picture', 'office', 'date_of_birth', 'password1', 'password2')