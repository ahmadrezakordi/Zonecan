from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Kelasor(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Parvande(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(null=True)
    file = models.FileField(upload_to='files/', null=True)
    kelasor = models.ForeignKey(Kelasor, related_name='parvandes', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
