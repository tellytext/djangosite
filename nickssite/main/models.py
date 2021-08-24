from django.db import models
from datetime import datetime

# Create your models here.
class Review(models.Model):
	review_title = models.CharField(max_length=200)
	review_content = models.TextField()
	review_date = models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.review_title	


class Categorie(models.Model):
	category_title = models.CharField(max_length=200)
	category_content = models.TextField()
	category_date = models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.category_title	


class Team(models.Model):
	team_title = models.CharField(max_length=200)
	team_content = models.TextField()
	team_date = models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.team_title

