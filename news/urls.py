from django.urls import path

from .views import home, one_post, new_base

urlpatterns = [
    path('', home,  name="home"),
    path('one_post/<int:post_id>/', one_post, name="one_post"),
    path('category/<int:id>/', new_base, name="new_base"),

]

