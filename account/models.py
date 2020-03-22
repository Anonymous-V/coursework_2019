from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    rating_user = models.PositiveIntegerField(default=0, blank=True)
    photo = ProcessedImageField(upload_to='users/',
                                blank=True,
                                null=True,
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 100})

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
