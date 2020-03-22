from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField


class AvailableLanguage(models.Model):
    lang = models.CharField(max_length=50, unique=True,
                            choices=settings.LANGUAGES)
    lang_code = models.CharField(max_length=5, unique=True,
                                 blank=True, null=True)
    image = ProcessedImageField(upload_to='language/',
                                blank=True,
                                null=True,
                                format='JPEG',
                                options={'quality': 60})
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        ordering = ['lang']

    def __str__(self):
        return self.get_lang_display()

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        super(AvailableLanguage, self).save(*args, **kwargs)


class Question(models.Model):
    title = models.CharField(max_length=250)
    language = models.ForeignKey(AvailableLanguage,
                                 on_delete=models.CASCADE, default='')
    author = models.ForeignKey(User, related_name='user_question',
                               on_delete=models.CASCADE, default='')
    body = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True)
    # answered = models.BooleanField(default=False, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
