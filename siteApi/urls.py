from rest_framework import routers
from . import views
from django.urls import path, include


urlpatterns=[
    path(r'get/profile/', views.get_user, name='get_user'),
    path(r'put/profile/', views.put_user, name='put_user'),
    path(r'patch/profile/', views.patch_user, name='patch_user'),
    path(r'like/<int:post_id>/', views.like, name='like'),
    path(r'post/<int:post_id>/', views.post, name='post'),
    path(r'post_comment/<int:post_id>/', views.post_comment, name='post_comment'),
    path(r'top-news/', views.top_news, name='top_news'),
    path(r'all-news/', views.PostsApiView.as_view({'get': 'list'}), name='all_news'),
    path(r'categories/', views.CatApiView.as_view({'get': 'list'}), name='cat'),

] 


router = routers.SimpleRouter()
# router.register(r'all-news', views.PostsApiView, basename='all_news')
# router.register(r'categories', views.CatApiView, basename='cat')

# router.register(r'post', views.PostApiViewSet, basename='post')
# router.register(r'get/profile', views.Profile, basename='profile')
# not working
# router.register(r'put/profile', views.PutProfile, basename='put_profile')
# router.register(r'patch/profile', views.PatchProfile, basename='patch_profile')

# router.register(r'token', include('rest_framework.urls'), basename='df')
# router.register(r'today', views.today, basename='today')




urlpatterns += router.urls