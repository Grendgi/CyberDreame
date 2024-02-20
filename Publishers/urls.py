from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.Publishers, name='Publishers'),
    path('page_all_news', views.all_news, name='page_all_news'),

    path('page_news_category/<int:category_id>/', views.news_by_category, name='page_news_category'),

    path('page_news_detail/<int:news_id>/', views.page_news_detail, name='page_news_detail'),
    path('create_news/', views.create_news_view, name='create_news'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
