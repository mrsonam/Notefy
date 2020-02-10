from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    item=models.CharField(max_length=200)
    notify_date = models.DateField("Notify Date: (mm/dd/y) eg.(2/2/2020)", auto_now_add=False, auto_now=False, blank=True, null=True)
    completed=models.BooleanField(default=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.item+ '|' + str(self.completed)
