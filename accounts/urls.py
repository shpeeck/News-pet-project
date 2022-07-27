from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterFormView.as_view(), name='register'),
    # path('register/', views.regist, name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]