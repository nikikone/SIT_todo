from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    file = models.FileField(blank=False, null=False)
    remark = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)


class ToDo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='todo', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class userProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
# Create your models here.
