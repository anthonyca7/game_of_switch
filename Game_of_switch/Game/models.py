"""from django.utils import timezone
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    games_won = models.IntegerField(default=0)
    games_lost = models.IntegerField(default=0)
    registration_dgate = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return self.username

class Friend(models.Model):
    user = models.ForeignKey(User)
    friend_username = models.CharField(max_length=20)
    date = models.DateTimeField()

    def __unicode__(self):
        return self.user

class Game(models.Model):
    user = models.ForeignKey(User)
    opponents = models.CharField(max_length=60)
    winner = models.CharField(max_length=20)
j
    def __unicode__(self):
        return self.user"""