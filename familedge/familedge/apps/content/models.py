from django.db import models

# Create your models here.
class disipline(models.Model):
	
	title=models.TextField()
	image=models.FileField(upload_to='images/')
	quote=models.TextField(default='this is suposed to be a quote')

	def __str__(self):
		return self.title
class article(models.Model):
	
	title=models.TextField()
	author=models.TextField()
	date=models.DateField()
	content=models.TextField()
	disipline=models.ForeignKey(disipline,on_delete=models.CASCADE,null=False)
	image=models.FileField(upload_to='images/')
	vues=models.IntegerField()

	def __str__(sefl):
		return self.title

	@staticmethod
	def disip_articles(d):
		return article.objects.filter(disipline=d)
	
	@staticmethod
	def arts_per_disip():
		
		aPerDis=[]
		for dis in disipline.objects.all() :
			r={'disipline':dis,'arts':article.disip_articles(dis)}
			aPerDis.append(r)

		return aPerDis
				
						
class quiz(models.Model):
	
	disipline=models.ForeignKey(disipline,on_delete=models.CASCADE,null=False)
	title=models.TextField()
	image=models.FileField(upload_to='images/',default='akr.jpg')

class qst(models.Model):
	
	quiz=models.ForeignKey(quiz,on_delete=models.CASCADE,null=False)
	description=models.TextField()
	reponse=models.TextField()
		
				
	

		