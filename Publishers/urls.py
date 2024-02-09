from django.urls import path

from . import views

urlpatterns = [
    path('', views.Publishers, name='Publishers'),
    path('page_all_news', views.page_all_news, name='page_all_news'),
    path('news', views.news, name='news'),
]
