from .models import GameProfile, UserProfile
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserForm, UserProfileForm, UpdatePasswordForm, GameProfileForm
from .forms import UserRegistrationForm



def Profile(request):
    game_profiles = request.user.game_profiles.all()
    return render(request, 'Profile/profile.html', {'game_profiles': game_profiles})


@login_required
def edit_profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.userprofile)
    game_profiles = request.user.game_profiles.all()

    if request.method == 'POST':
        user = request.user
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)

        # Проверяем, передано ли новое имя пользователя
        username = request.POST.get('username')
        if username and username != user.username:
            user.username = username
            user.save()

        # Проверяем, передана ли новая информация "О себе"
        bio = request.POST.get('about')
        if bio:
            user.userprofile.bio = bio
            user.userprofile.save()

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('Profile')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
        game_profiles = request.user.game_profiles.all()

    return render(request, 'Profile/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'game_profiles': game_profiles
    })


@login_required
def update_avatar(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('Profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'Profile/edit_profile.html', {'form': form})

@login_required
def update_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        current_password = request.POST.get('current_password')
        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            user.email = new_email
            user.save()
            messages.success(request, 'Ваш email был успешно обновлен.')
            return redirect('Profile')  # или куда вам нужно
        else:
            messages.error(request, 'Предоставлен неверный пароль.')

    # Если это GET запрос или есть другие ошибки, возвращаем пользователя на страницу редактирования
    return redirect('edit_profile')

@login_required
def update_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Обновляем сессию, чтобы не выходить из системы
            messages.success(request, 'Ваш пароль был успешно изменен.')
            return redirect('Profile')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'Profile/edit_profile.html', {'form': form})

@login_required
def update_profile(request):
    # Обработка обновления данных профиля
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('Profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'Profile/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def add_game_profile(request):
    if request.method == 'POST':
        form = GameProfileForm(request.POST)
        if form.is_valid():
            game_profile = form.save(commit=False)
            game_profile.user = request.user
            game_profile.save()
            # Возвращаем данные в формате JSON
            return JsonResponse({
                'id': game_profile.id,
                'game_name': game_profile.game_name,
                'character_name': game_profile.character_name
            })
        else:
            # Возвращаем ошибку валидации в формате JSON
            return JsonResponse({'error': 'Неверные данные формы'}, status=400)


@login_required
def delete_game_profile(request, profile_id):
    if request.method == 'POST':
        try:
            profile = GameProfile.objects.get(id=profile_id, user=request.user)
            profile.delete()
            return JsonResponse({'status': 'success', 'message': 'Профиль успешно удален.'})
        except GameProfile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Профиль не найден.'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Неверный запрос.'}, status=400)



def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return redirect('Profile')  # Замените на ваш URL
        else:
            return JsonResponse(form.errors, status=400)
    return JsonResponse({'status': 'error'}, status=400)

# Функция для входа пользователя
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('Profile')
        else:
            return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'status': 'error'}, status=400)