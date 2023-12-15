from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, UserChangeForm
from django.contrib.auth.forms import forms
from django.forms import PasswordInput

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
    email = forms.EmailField(required=True)
    password = forms.CharField(label="Пароль", widget=PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Имя', max_length=100, required=True)
    last_name = forms.CharField(label='Фамилия', max_length=100, required=True)
    second_name = forms.CharField(label='Отчество', max_length=100, required=True)
    group = forms.CharField(label='Группа', max_length=10, required=True)
    subgroup = forms.CharField(label='Подгруппа', max_length=10, required=False)
    id_card = forms.IntegerField(label='Номер ст. билета', min_value=0, max_value=9999999)
    is_mag = forms.BooleanField(label='Форма обучения')

    class Meta:  # define a metadata related to this class
        model = Student
        fields = (
            'email',
            'first_name',
            'last_name',
            'second_name',
            'group',
            'id_card',
            'is_mag',
            'password1',
            'password2',

        )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.second_name = self.cleaned_data['second_name']
        user.group = self.cleaned_data['group']
        user.id_card = self.cleaned_data['id_card']
        user.is_mag = self.cleaned_data['is_mag']

        if commit:
            user.save()  # running sql in database to store data
        return user

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Student
        fields = ('email', 'first_name', 'last_name', 'second_name', 'group', 'is_mag', 'id_card')
