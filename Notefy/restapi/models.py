from django.db import models

# Create your models here.
class ApiModel(models.Model):
    user_name = models.CharField(max_length=20)
    user_address = models.CharField(max_length=20)
    user_contact = models.IntegerField()

    def __str__(self):
        return self.user_name