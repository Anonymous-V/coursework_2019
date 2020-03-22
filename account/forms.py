from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django import forms
import os
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Логин на сайте'),
                               widget=forms.TextInput(
                                   attrs={'placeholder': _('Введите Ваш логин'),
                                          'class': 'full-width'}
                               ))
    password = forms.CharField(label=_('Пароль для входа'),
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': _('Введите Ваш пароль'),
                                          'class': 'full-width'}
                               ))
    next = forms.CharField(widget=forms.HiddenInput(), required=False)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_('Пароль для входа'),
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': _('Придумайте пароль не менее 6 символов'),
                                          'class': 'full-width'}
                               ))
    password2 = forms.CharField(label=_('Повторите пароль'),
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': _('Повторите пароль записанный выше'),
                                           'class': 'full-width'}
                                ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        labels = {
            'username': _('Логин на сайте'),
            'first_name': _('Как Вас зовут?'),
            'email': _('Ваш Email')
        }
        help_texts = {
            'username': None
        }
        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Ivanov_1',
                       'class': 'full-width'},
            ),
            'first_name': forms.TextInput(
                attrs={'placeholder': _('Иванов Иван Иванович'),
                       'class': 'full-width'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Ivanov@mailbox.com',
                       'class': 'full-width'}
            ),

        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)
        labels = {
            'photo': _('Ваша фотография (необязательно)')
        }
