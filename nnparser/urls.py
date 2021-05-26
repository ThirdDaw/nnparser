from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cv/', views.cv, name='cv'),
    path('sds/', views.sds, name='sds'),
]