import django.forms as forms
from django.forms.widgets import PasswordInput

class Forms(forms.Form):
    name = forms.CharField(label="Name\n", max_length=50)
    age = forms.CharField(label="Age\n", max_length=3)
    username = forms.CharField(label="Username\n", max_length=15)
    password = forms.CharField(label="Password\n", max_length=20, widget=PasswordInput)