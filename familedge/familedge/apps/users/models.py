import datetime
from django.db import models
from ..content.models import quiz,disipline

# Create your models here.
class family(models.Model):
	
	name=models.TextField(primary_key=True)
	score=models.IntegerField()

	def __str__(self):
		return self.name

class user(models.Model):
	
	name=models.TextField()
	password=models.TextField()
	family=models.ForeignKey(family,on_delete=models.CASCADE,null=False)

	def __str__(self):
		return self.name;
	
	def family(self):
		try:
			return family.objects.get(name=self.family)
		except:
			return None
		
	@staticmethod	
	def connect(n,p):
		try:
			return user.objects.get(name=n,password=p)
		except:
			return None
class user_disipline(models.Model):
	
	disipline=models.ForeignKey(disipline,on_delete=models.CASCADE,null=False)
	user=models.ForeignKey(user,on_delete=models.CASCADE,null=False)

	@staticmethod
	def user_disip(u):
		return user_disip.objects.filter(user=u)

	@staticmethod
	def disipline_users(d):
		return user_disip.objects.filter(disipline=d)
class userbis(models.Model):
	
	user=models.ForeignKey(user,on_delete=models.CASCADE,null=False)
	cooki=models.TextField()

	@staticmethod
	def is_valid(c):
		try:
			u=userbis.objects.get(cooki=c)		
			return u.user
		except:
			return None
	@staticmethod
	def add_cooki(u,c):
		userbis.objects.create(user=u,cooki=c)
	@staticmethod
	def rmcooki(c):
		userbis.objects.filter(cooki=c).delete()	

class history(models.Model):
	
	user=models.ForeignKey(user,on_delete=models.CASCADE,null=False)
	quiz=models.ForeignKey(quiz,on_delete=models.CASCADE)
	score=models.IntegerField()
	date=models.DateField()

	@staticmethod
	def add_hist(u,q,s):
		try:
			history.objects.create(user=u,quiz=q,score=s,date=datetime.date.today())		
			return True
		except :
			return False
	@staticmethod
	def user_hist(u):
		return history.objects.filter(user=u)

class objective(models.Model):

	user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
	deadline=models.DateField()
	progress=models.IntegerField(default=0)
	goal=models.IntegerField()

	@staticmethod
	def new_objective(u,g,p):
		objective.objects.create(user=u,deadline=(datetime.date.today() + relativedelta(months=1)),goal=g)

	@staticmethod
	def get_current_objective(u):
		try:
			return objective.objects.get(user=u)
		except:
			return None			
		

		

			
		




			

		

