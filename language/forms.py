from django import forms


class AddLanguage(forms.Form):
    code = forms.CharField(max_length=5,
                           label='Код языка',
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Введите код языка',
                                      'class': 'full-width'}
                           ))
    language = forms.CharField(max_length=20,
                               label='Название языка',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Введите название языка',
                                          'class': 'full-width'}
                               ))
