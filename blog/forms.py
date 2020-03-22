from django.utils.translation import gettext as _
from django import forms
from .models import Comments
from account.models import Profile
import os


class CommentForm(forms.ModelForm):
    message = forms.Textarea()

    class Meta:
        model = Comments
        fields = ('message', 'audio',)

        labels = {
            'message': _('Комментарий к вопросу'),
            'audio': _('Аудиофайл')
        }

        widgets = {
            'message': forms.Textarea(
                attrs={'placeholder': _('Ваш комментарий'),
                       'class': 'full-width'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['audio'].widget.attrs.update({'class': 'full-width'})

    def clean_audio(self):
        file = self.cleaned_data['audio']
        print(file)
        if not file:
            return None
        # if not file.content-type in ['audio/mpeg', 'audio/...']:
        #     raise forms.ValidationError('Content-Type is not mpeg')
        if not os.path.splitext(file.name)[1] in ['.mp3', '.wav']:
            raise forms.ValidationError('This is no audio file')
        return file


class RatingForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('rating_user',)
