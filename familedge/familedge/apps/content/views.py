from django.shortcuts import render
from familedge.functions import checkuser
from .models import *
from ..users.models import user_disipline,goals
# Create your views here.

def home(request):
	
	disipline_list = disipline.objects.all()
	articles_list = article.objects.all()
	disip_articles = article.arts_per_disip()

	user = checkuser(request)
	if user == None:
		return render(request,'home.html',{'home':True ,'connected':False,'disipline_list':disipline_list,'articles_list':articles_list,'disip_articles':disip_articles})

	users_disipline = user_disipline.user_disip(user)
	users_articles = []
	for d in users_disipline:
		for art in article.disip_articles(d):
			users_articles.append(art)

	return render(request,'home.html',{'home':True ,'connected':True,'disipline_list':users_disipline,'articles_list':users_articles,'disip_articles':disip_articles})
		
def post(request):
	connected=True
	user = checkuser(request)
	if user == None:
		connected=False
	articles_list = article.objects.all()
	disipline_list = disipline.objects.all()
	objcts=goals.objects.all()
	if request.method == "GET":
		try:
			art=article.objects.get(id=request.GET.get('article_id'))
			art.vues+=1
			art.save()
			qz=quiz.objects.filter(disipline=art.disipline)
		except:
			art=None
			

	return render(request,'post.html',{'connected':connected,'article':art,'objcts':objcts,'disipline_list':disipline_list,'articles_list':articles_list,'quiz':qz,})

def quizView(request):
	connected=True
	user = checkuser(request)
	if user == None:
		connected=False

	disip_quiz=[]
	for d in disipline.objects.all():
		disip_quiz.append({'disipline':d,'quiz':quiz.objects.filter(disipline=d)})

	try:
		if request.method == "GET":
			qz=quiz.objects.get(id=request.GET.get('quiz_id'))
			qs=qst.objects.filter(quiz=qz)
			play_quiz={'quiz':qz,'qst':qs}
	except:
		play_quiz=None





	return render(request,'quiz.html',{'connected':connected,'disip_quiz':disip_quiz,'play_quiz':play_quiz})