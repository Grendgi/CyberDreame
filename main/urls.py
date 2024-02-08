from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('section1/', views.section1, name='section1'),
    path('section2/', views.section2, name='section2'),
    path('section3/', views.section3, name='section3'),
    path('section4/', views.section4, name='section4'),
    path('section5/', views.section5, name='section5'),
    path('section6/', views.section6, name='section6'),
]