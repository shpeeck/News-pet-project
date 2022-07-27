from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView

# Подключение для рендера
from django.shortcuts import render
from .forms import RegistrForm

class RegisterFormView(FormView):
    form_class = RegistrForm
    success_url = reverse_lazy('register')
    template_name = "registration/register.html"

    def form_valid(self, form):
        print('dfsdfsfssdfsdsdfsf', form)
        # form.save()
        return super().form_valid(form)

# def regist(request):
#     # Массив для передачи данных шаблонны
#     data = {}
#     # Проверка что есть запрос POST
#     if request.method == 'POST':
#         # Создаём форму
#         form = RegistrForm(request.POST)
#         # Валидация данных из формы
#         if form.is_valid():
#             # Сохраняем пользователя
#             # form.save()
#             print(form)
#             # Передача формы к рендару
#             data['form'] = form
#             # Передача надписи, если прошло всё успешно
#             data['res'] = "Всё прошло успешно"
#             # Рендаринг страницы
#             return render(request, 'registration/register.html', data)
#     else: # Иначе
#         # Создаём форму
#         form = RegistrForm()
#         # Передаём форму для рендеринга
#         data['form'] = form
#         # Рендаринг страницы
#         return render(request, 'registration/register.html', data)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = "registration/login.html"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))