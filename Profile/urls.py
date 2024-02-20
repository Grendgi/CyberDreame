from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.Profile, name='Profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('update_avatar/', views.update_avatar, name='update_avatar'),
    path('update_email/', views.update_email, name='update_email'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('add_game_profile/', views.add_game_profile, name='add_game_profile'),
    path('delete_game_profile/<int:profile_id>/', views.delete_game_profile, name='delete_game_profile'),

    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
]