from django.db import models

class Account(models.Model):
    registerID = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.login

