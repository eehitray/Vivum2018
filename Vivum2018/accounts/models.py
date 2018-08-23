from django.db import models
from django.contrib.auth.models import User

class FalseUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	height = models.FloatField(default='-1')
	weight = models.FloatField(default='-1')
	age = models.IntegerField(default='-1')
	gender = models.CharField(max_length=1, default='M')
	activity = models.CharField(max_length=200, default='invalid')
