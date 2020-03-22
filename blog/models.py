from django.db import models
from question.models import Question
from django.contrib.auth.models import User


class Comments(models.Model):
    post = models.ForeignKey(Question, related_name='comments',
                             on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='user_comments',
                               on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    best_answer = models.BooleanField(default=False, blank=True)
    audio = models.FileField(upload_to='audio_comment/', blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post)
