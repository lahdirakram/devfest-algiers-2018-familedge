from django.db import models

# Create your models here.
class disipline(models.Model):
	
	title=models.TextField()

	def __str__(self):
		return self.title
class article(models.Model):
	
	title=models.TextField()
	author=models.TextField()
	date=models.DateField()
	content=models.TextField()
	disipline=models.ForeignKey(disipline,on_delete=models.CASCADE,null=False)

	def __str__(sefl):
		return self.title

	@staticmethod
	def disip_articles(d):
		return article.objects.filter(disipline=d)
				
class quiz(models.Model):
	
	disipline=models.ForeignKey(disipline,on_delete=models.CASCADE,null=False)
	title=models.TextField()

class qst(models.Model):
	
	quiz=models.ForeignKey(quiz,on_delete=models.CASCADE,null=False)
	description=models.TextField()
	reponse=models.TextField()
		
				
	

		