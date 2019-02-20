from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import LoginForm, UserRegistrationForm, ProfileForm
from .models import Profile


def user_login(request):
    return_page = reverse('index_page')
    if 'next' in request.GET:
        return_page = request.GET.get('next')
        messages.add_message(request, messages.ERROR,
            _('Данная страница доступна только<br>авторизированным пользователям'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(return_page)
                else:
                    return HttpResponse(_('Отключенный аккаунт'))
            else:
                form = LoginForm(request.POST)
                form.add_error(None, _('Проверьте правильность введенных Вами данных'))
                return render(request, 'registration/login.html', {'form': form})
        else:
            form = LoginForm(request.POST)
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            new_user.refresh_from_db()

            new_profile = Profile.objects.create(user=new_user,
                                                 photo=profile_form.cleaned_data['photo'])
            new_profile.save()

            return render(request, 'registration/register_done.html', {
                'new_user': new_user,
                'new_profile': new_profile
            })
        else:
            user_form = UserRegistrationForm(request.POST)
            new_profile = ProfileForm(data=request.POST, files=request.FILES)
        # return render(request, 'registration/register.html', {
        #     'user_form': user_form,
        #     'new_profile': new_profile
        # })
    else:
        user_form = UserRegistrationForm()
        new_profile = ProfileForm()
    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'new_profile': new_profile
    })
