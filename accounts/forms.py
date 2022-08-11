from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from . import views


User = get_user_model()


class UserCreation(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254, help_text='*')
    first_name = forms.CharField(label='Имя', required=True, max_length=50)
    last_name = forms.CharField(label='Фамилия', required=True, max_length=50)
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Почта'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'


class RegistrForm(UserCreationForm):
    email = forms.EmailField(label='Email', max_length=254, help_text='*')
    first_name = forms.CharField(label='Имя', required=True, max_length=50)
    last_name = forms.CharField(label='Фамилия', required=True, max_length=50)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Почта'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Фамилия'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
