"""DigitalStory URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.entrance, name = 'DS_entrance'),

    path('partI_1/', views.partI_1, name = 'partI_1'),
    path('partI_2/', views.partI_2, name = 'partI_2'),
    path('partI_3/', views.partI_3, name = 'partI_3'),

    path('partII_1/', views.partII_1, name = 'partII_1'),
    path('partII_2/', views.partII_2, name = 'partII_2'),
    path('partII_3/', views.partII_3, name = 'partII_3'),

    path('partIII_1/', views.partIII_1, name = 'partIII_1'),
    path('partIII_2/', views.partIII_2, name = 'partIII_2'),
    path('partIII_3/', views.partIII_3, name = 'partIII_3'),

    path('about/', views.about, name = 'About'),
]
