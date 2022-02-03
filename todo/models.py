from django.db import models

# Create your models here.

class task(models.Model):
	title = models.CharField(max_length=200)
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	due = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)

	def __str__(self):
		return self.title

