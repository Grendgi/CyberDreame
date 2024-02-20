from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import UserProfile, GameProfile


class UserForm(UserChangeForm):
    password = None  # Исключаем поле пароля из формы
    class Meta:
        model = User
        fields = ['username', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio']


class UpdatePasswordForm(PasswordChangeForm):
    # Эта форма уже есть в Django и включает в себя валидацию старого и нового пароля
    pass


class GameProfileForm(forms.ModelForm):
    class Meta:
        model = GameProfile
        fields = ['game_name', 'character_name']






class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

