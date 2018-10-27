from django.shortcuts import render,redirect,redirect
from .models import *
from familedge.functions import checkuser
from django.http import HttpResponse,JsonResponse
from django.utils.crypto import get_random_string
import json
# Create your views here.
def connect(request):
	
	if request.method == "POST":
		u=user.connect(request.POST.get('username'),request.POST.get('password'))
		if(u!=None):
			rand=get_random_string(length=128)
			response=redirect('home')
			response.set_cookie('remember_me',rand,max_age=3600*24*10)
			userbis.add_cooki(u,rand)
			return response
		else:
			return redirect('home')

def deconnect(request):
	
	if 'remember_me' in request.COOKIES:
		userbis.rmcooki(request.COOKIES['remember_me'])

	response= redirect('home')
	response.delete_cookie('check_in')
	response.delete_cookie('remember_me')
	return response			

def hist(request):
	
	user = checkuser(request)
	if user == None:
	 	return redirect('landpage')

	if request.method=="POST":
		history.add_hist(user,quiz.objects.get(id=request.POST.get('quiz_id')),request.POST.get('sc'))
		return JsonResponse({'reponse':request.POST.get('sc')})

def objective(request):
	
	user = checkuser(request)
	if user == None:
	 	return redirect('home')
	 	print(user)

	try:
		obj=goals.objects.get(user=user)
		if obj.progress < obj.goal:
			obj.progress+=1
			obj.save()
	except:
		obj=None

	return redirect('home')

def dashboard(request):
	connected=True
	u = checkuser(request)
	if u == None:
		return redirect('home')

	o=goals.get_current_objective(u)
	hist=[]
	for onehist in history.objects.raw("select id,user_id,count(quiz_id) nbrquiz,sum(score) sumscore from users_history group by user_id order by sum(score) desc"):
		hist.append({'user':user.objects.get(id=onehist.user_id),'nbrquiz':onehist.nbrquiz,'sumscore':onehist.sumscore})

	graphdata=[]
	for a in family.members(u.fami):
		onemember={'name':a.name,'data':[]}
		for onegraph in history.objects.raw('select id,date,count(quiz_id) nbrquiz,sum(score) sumscore from users_history where user_id ='+str(a.id)+' order by date desc'):
			onemember['data'].append([onegraph.date.strftime("Date.UTC(%Y,%m,%d)"),onegraph.sumscore])
		graphdata.append(onemember)

	resu = json.dumps(graphdata)	


	print(resu)


	return render(request,'dashboard.html',{'connected':connected,'obj':o,'hist':hist,'graphdata':resu})
