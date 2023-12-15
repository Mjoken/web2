from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm
from django.contrib.auth.forms import forms

from students.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('email', 'first_name', 'last_name', 'second_name', 'group', 'subgroup', 'is_mag', 'id_card')


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(label="Адрес эл. почты", widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'AllEgg@mail.ru',
               'id': 'email',
               'title': 'Электронная почта',
               'name': 'username',
               }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ваш пароль',
            'id': 'password',
            'title': 'Пароль'
        }
    ))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ('email', 'password')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ('email', 'first_name', 'last_name', 'second_name', 'group', 'is_mag', 'id_card')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Student
        fields = ('email', 'first_name', 'last_name', 'second_name', 'group', 'is_mag', 'id_card')
