from django import forms
from .models import DataPoint
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class DataPointForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = ('x', 'y')
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser