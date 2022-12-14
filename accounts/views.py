from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

from django.shortcuts import render
from .forms import RegistrForm, UserCreation, ProfileForm

from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import LoginView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


def send_mail_verify(request, user):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
    }
    message = render_to_string('registration/verify.html',context = context,)
    email = EmailMessage('Verify email', message, to=[user.email],)
    email.send()


User = get_user_model()


class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except:
            user = None
        return user


class RegisterFormView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreation()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            send_mail_verify(request, user)
            return redirect('confirm')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class MyLoginView(LoginView):
    form_class = AuthenticationForm
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def form_valid(self, form):
        self.user = form.get_user()
        if self.user.email_verify:
            if self.user.user_active:
                login(self.request, self.user)
                return super().form_valid(form)
            else:
                return redirect('blocked')
        else:
            send_mail_verify(self.request, self.user)
            return redirect('confirm')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))


def user(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'registration/user.html', context={'user': user})
    else:
        return redirect(reverse('mylogin'))

def user_update(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('mylogin'))

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name'] 
            user.last_name = form.cleaned_data['last_name']
            user.save()
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name}
        form = ProfileForm(default_data)
    return render(request, 'registration/update.html', {'form': form, 'user': user})


