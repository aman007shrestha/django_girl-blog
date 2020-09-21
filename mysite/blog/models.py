from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinLengthValidator
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100,
		validators=[MinLengthValidator(2, "Minimum 2 characters required")])
	text = models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(null=True, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title




