from django import forms
from django.contrib.auth.models import User
from basicapp.models import Userprofileinfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        #now password above one will be taken instead of built in attribute
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ('portfolio_site','profile_pic')
