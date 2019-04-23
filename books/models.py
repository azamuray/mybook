from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=120)
	author = models.CharField(max_length=120)
	image = models.ImageField(
		null=True, blank=True,
		upload_to='images/',
		verbose_name='Изображение'
		)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('news:post-detail', kwargs={'pk': self.pk})