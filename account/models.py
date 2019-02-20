from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    photo = ProcessedImageField(upload_to='users/',
                                blank=True,
                                null=True,
                                processors=[ResizeToFill(300, 300)],
                                format = 'JPEG',
                                options={'quality': 100})

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)