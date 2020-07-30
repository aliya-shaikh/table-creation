from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Table(models.Model):
	title = models.CharField(max_length = 100)
	content = RichTextField(blank=True, null=True)
	author = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home')