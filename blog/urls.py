from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add', views.add, name='add'),
    path('multiple', views.multiple, name='multiple'),
    path('submission', views.submission, name='submission'),
]
