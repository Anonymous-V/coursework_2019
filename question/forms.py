from django.utils.translation import gettext as _
from django import forms
import os
from .models import Question


class UserQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'language', 'body', 'audio')

        labels = {
            'title': _('Название вопроса'),
            'language': _('Выберите язык'),
            'body': _('Текст вопроса'),
            'audio': _('Аудио (необязательно)')
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': _('Введите название вопроса'),
                       'class': 'full-width'},
            ),
            'body': forms.Textarea(
                attrs={'placeholder': _('Введите текст вопроса'),
                       'class': 'full-width'}
            ),
        }

    # Модифицирование стандартных виджетов
    def __init__(self, *args, **kwargs):
        super(UserQuestion, self).__init__(*args, **kwargs)
        self.fields['audio'].widget.attrs.update({'class': 'full-width'})
        self.fields['language'].widget.attrs.update({'class': 'full-width'})

    def clean_audio(self):
        file = self.cleaned_data['audio']
        if not file:
            return None
        # if not file.content-type in ['audio/mpeg', 'audio/...']:
        #     raise forms.ValidationError('Content-Type is not mpeg')
        if not os.path.splitext(file.name)[1] in ['.mp3', '.wav']:
            raise forms.ValidationError('This is no audio file')
        return file

#     http://qaru.site/questions/302487/django-audio-file-validation
