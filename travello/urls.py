from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # import re_path and do the same
    # path('destination/add', views.add_destination, name="destination_add"),
    re_path('bill/(?P<unique_id>[\w-]+)', views.bill_view, name='bill')
]
