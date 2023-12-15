from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm, UserChangeForm
from django.contrib.auth.forms import forms
from .models import *
class SessionDetails(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ('group', 'title', 'short_title', 'session_type', 'subgroup')

        widgets = {
            'date': forms.DateInput(format='yyyy-MM-dd', attrs={'type': 'date', 'id': 'date_start'}),
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }