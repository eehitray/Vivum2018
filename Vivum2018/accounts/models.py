from django.db import models
from django.contrib.auth.models import User

class FalseUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	height = models.FloatField(default='-1')
	weight = models.FloatField(default='-1')
	age = models.IntegerField(default='-1')
	gender = models.CharField(max_length=1, default='M')
	calorieGoal = models.IntegerField(default='-1')
	calorieDate = models.DateField(null=True, blank=True)

	def __str__(self):
		return user.get_username()
