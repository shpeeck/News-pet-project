from django.urls import path

from .views import home, post, politic, busines, sport, fashion, travel

urlpatterns = [
    path('', home,  name="home"),
    path('post/<int:post_id>/', post, name="post"),
    path('politic/', politic, name="politic"),
    path('busines/', busines, name="busines"),
    path('sport/', sport, name="sport"),
    path('fashion/', fashion, name="fashion"),
    path('travel/', travel, name="travel"),
]
