from django.shortcuts import render,redirect,redirect
from .models import *
from familedge.functions import checkuser
from django.http import HttpResponse,JsonResponse
from django.utils.crypto import get_random_string
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
		
		return JsonResponse({'reponse':history.add_hist(user,quiz.objects.get(id=request.POST.get('quiz_id')),request.POST.get('sc'))})

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
	user = checkuser(request)
	if user == None:
		return redirect('home')

	o=goals.get_current_objective(user)

	return render(request,'dashboard.html',{'connected':connected,'obj':o})
