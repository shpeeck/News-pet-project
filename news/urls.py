from django.urls import path

from .views import home, foo

urlpatterns = [
    path('', home,  name="home"),
    path('test/', foo,  name="foo")
]
