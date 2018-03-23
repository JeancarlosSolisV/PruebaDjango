from django.conf.urls import url,include,path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    url(r'', views.index, name='index'),
]