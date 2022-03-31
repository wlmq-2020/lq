from django.urls import path,re_path
from app import views


regular = r'(?P<year>\d{4})/(?P<month>\d{1,2})'
urlpatterns = [
    path('', views.timestr),
    path('times/', views.timestr),
    path('login/', views.login),
    path('auth/', views.auth),
    re_path(regular, views.articles),\

]
