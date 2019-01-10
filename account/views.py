from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import LoginForm, UserRegistrationForm, ProfileForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('index_page'))
                else:
                    return HttpResponse('Disabled account')
            else:
                form = LoginForm(request.POST)
                form.add_error(None, 'Проверьте правильность введенных Вами данных')
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

            new_profile = Profile.objects.create(user=new_user, photo=request.FILES['photo'])
            new_profile.save()

            return render(request, 'registration/register_done.html', {
                'new_user': new_user,
                'new_profile': new_profile
            })
        else:
            user_form = UserRegistrationForm(request.POST)
            new_profile = ProfileForm(data=request.POST, files=request.FILES)
        return render(request, 'registration/register.html', {
            'user_form': user_form,
            'new_profile': new_profile
        })
    else:
        user_form = UserRegistrationForm()
        new_profile = ProfileForm()
    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'new_profile': new_profile
    })
