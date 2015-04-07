from django.db import models

# Create your models here.



class Post(models.Model):
	title= models.CharField(max_length=255)
	body= models.TextField(max_length=2000)
	created_at = models.DateTimeField()



	def __unicode__(self):
		return self.title


		
