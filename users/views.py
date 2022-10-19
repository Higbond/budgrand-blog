from django.shortcuts import render, redirect
from .forms import UserRegForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('home')

    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'title': 'Страница регистрации', 'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Ваш акаунт был успешно обновлен')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'updateUserForm': updateUserForm})