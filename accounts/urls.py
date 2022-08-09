from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('login/', views.MyLoginView.as_view(), name='mylogin'),
    path('logout/', views.LogoutView.as_view(), name='mylogout'),
    # path('', include('django.contrib.auth.urls')),
    path('confirm/', TemplateView.as_view(template_name='registration/confirm.html'), name='confirm'),
    path('blocked/', TemplateView.as_view(template_name='registration/blocked.html'), name='blocked'),
    path('verify/<uidb64>/<token>/', views.EmailVerify.as_view(), name='verify'),
    path('invalid/', TemplateView.as_view(template_name='registration/invalid.html'), name='invalid'),
    path('user/', views.user, name='user'),
    path('user/update/', views.user_update, name='profile_update'),
]