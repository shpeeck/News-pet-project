from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate
from . import views


User = get_user_model()


class UserCreation(UserCreationForm):
    # username = forms.CharField(label='Имя', required=True, max_length=50)
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

    # error_messages = {
    #     'password_mismatch': ("Пароли не совпадают."),
    #     'error': ("Форма не валидна."),
    #     'email_exists': ("Пользователь с таким email уже существует."),
    # }
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

# class MyAuthenticationForm(AuthenticationForm):
#     def clean(self):
#         username = self.cleaned_data.get('username')
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')
#         print('e', email, password)

#         if username is not None and password:
#             self.user_cache = authenticate(self.request, username=email, password=password)
#             print('email is Nine')
        #     if not self.user_cache.email_verify:
        #         views.send_mail_verify(self.request, self.user_cache)
        #         print('error1')
        #     #     raise ValidationError(
        #     # 'Check email for verify', code='invalid_login')
        #     if self.user_cache is None:
        #         # raise self.get_invalid_login_error()
        #         print('error2')
        #     else:
        #         self.confirm_login_allowed(self.user_cache)
        # return self.cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        # self.fields['email'].help_text = None
        # self.fields['first_name'].help_text = None
        # self.fields['last_name'].help_text = None
        # self.fields['password2'].help_text = None


# class PostForm(forms.ModelForm ):
#     class Meta:
#         model = Books
#         fields = ['title', 'released_year', 'description', 'author']

# class CommentForm(forms.ModelForm):
#     body = forms.CharField(widget=forms.Textarea, label='')
#     class Meta:
#         model = Comments
#         fields = ['body']

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
