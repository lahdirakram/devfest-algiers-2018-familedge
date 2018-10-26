from django.shortcuts import render
from familedge.functions import checkuser
from .models import disipline,article,quiz,qst
from ..users.models import user_disipline
# Create your views here.

def home(request):
	
	user = checkuser(request)
	if user == None:
	 	return redirect('landpage')

	disipline_list = disipline.objects.all()
	articles_list = article.objects.all()

	users_disipline = user_disipline.user_disip(user)
	users_articles = []
	for disipline in users_articles:
		users_articles.append(article.disip_articles(disipline))



		
