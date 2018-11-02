from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	education = models.CharField(max_length=120)
	degree = models.CharField(max_length=120)
	caption = models.TextField()
	skills = models.CharField(max_length=120)

	def __str__(self):
		return f'{self.user.username} Profile'

	# to override the size of large images to 300 300
	def save(self, force_insert=False, force_update=False, *args, **kwargs):
		super().save()

		img = Image.open(self.image.path)

		if img.height < 300 or img.width < 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)