from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('citi', views.citi, name='citi'),
    path('statements', views.citi)
]