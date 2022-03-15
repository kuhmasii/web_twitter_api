from django.db import models

class Page(models.Model):
	title = models.CharField(max_length=100)
	permalink = models.CharField(max_length=50)
	body_text = models.TextField('Page content', blank=True, null=True)
	update_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.title