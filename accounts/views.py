from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

from django.shortcuts import render
from .forms import RegistrForm, UserCreation

# email
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail
from django.contrib.auth.views import LoginView


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
            print('no user')
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
            # username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=password)
            send_mail_verify(request, user)
            return redirect('confirm')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


# class LoginFormView(FormView):
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('home')
#     template_name = "registration/login.html"

#     def form_valid(self, form):
#         self.user = form.get_user()
#         login(self.request, self.user)
#         return super().form_valid(form)

class MyLoginView(LoginView):
    form_class = AuthenticationForm

    def form_valid(self, form):
        self.user = form.get_user()
        if self.user.email_verify == True:
            login(self.request, self.user)
            return super().form_valid(form)
        else:
            send_mail_verify(self.request, self.user)
            return redirect('confirm')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))
