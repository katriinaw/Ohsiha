from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='menoappi'),
    path('haku/', views.haku, name='haku'),
]
