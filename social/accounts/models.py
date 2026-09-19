from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField()
    is_current_user = models.BooleanField()

    def __str__(self):
        return self.username