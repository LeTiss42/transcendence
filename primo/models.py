from django.db import models

class Champignon(models.Model):
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=200)

	def __str__(self):
		return self.name + ' de type ' + self.type