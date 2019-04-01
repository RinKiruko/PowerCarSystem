from django.db import models
# from django.contrib.auth.models import AbstractUser
from authtools.models import AbstractEmailUser


class User(AbstractEmailUser):
	pass
	FirstName = models.CharField(null=True,verbose_name='Имя', max_length=50)
	LastName = models.CharField(null=True,verbose_name='Фамилия', max_length=50)
	def __str__(self):
		return self.FirstName + self.LastName
