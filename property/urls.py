from django.urls import path

from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    path('get-details', views.get_details, name='get_details'),
]
