from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    note_title = models.CharField(max_length=20)
    note_content = models.TextField()
    note_images = models.ImageField(upload_to='images', null=True, blank = True)
    note_audio = models.FileField(upload_to='audios', null=True, blank = True)
    note_videos = models.FileField(upload_to='videos', null=True, blank = True)
    note_password = models.CharField(max_length=50, null=True, blank = True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_title

    def delete(self, *args, **kwargs):
        self.note_images.delete()
        self.note_audios.delete()
        self.note_videos.delete()
        super(Note, self).delete(*args, **kwargs)

