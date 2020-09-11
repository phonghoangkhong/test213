from django.urls import path
from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()
from polls import view

urlpatterns = [
    path('', view.index, name='index')
]
