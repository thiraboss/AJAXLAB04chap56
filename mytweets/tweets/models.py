from django.db import models
from user_profile.models import User
# Create your models here.

class Tweet(models.Model):

	"""
	Tweet model
	"""
	user = models.ForeignKey(User,on_delete=models.DO_NOTHING,) 
	text = models.CharField(max_length=160) 
	created_date = models.DateTimeField(auto_now_add=True) 
	country = models.CharField(max_length=30) 
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.text
		
class HashTag(models.Model):
	"""
	HashTag model
	"""
	name = models.CharField(max_length=64, unique=True)
	tweet = models.ManyToManyField(Tweet)
	def __unicode__(self):
		return self.name