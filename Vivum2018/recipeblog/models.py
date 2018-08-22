from django.db import models
import json

class Post(models.Model):
	title = models.CharField(max_length=100)
	ingredients = models.CharField(max_length=10000)
	contents = models.TextField()
	picture = models.URLField(max_length=500)
	datePosted = models.DateTimeField('Date published')

	def setIngredients(self, ingredientsText):
		self.ingredients = json.dumps(ingredientsText)

	def getIngredientsList(self):
		return json.loads(self.ingredients)
	
	def __str__(self):
		return self.title