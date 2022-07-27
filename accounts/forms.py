from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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