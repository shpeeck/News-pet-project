from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    # path('register/', views.regist, name='register'),
    # path('login/', views.LoginFormView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('confirm/', TemplateView.as_view(template_name='registration/confirm.html'), name='confirm'),
    path('verify/<uidb64>/<token>/', views.EmailVerify.as_view(), name='verify'),
    path('invalid/', TemplateView.as_view(template_name='registration/invalid.html'), name='invalid'),
    path('user/', views.user, name='user'),
    path('user/update/', views.user_update, name='profile_update')
]