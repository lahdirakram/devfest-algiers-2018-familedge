from django.shortcuts import render,redirect,redirect
from .models import user,userbis
from django.http import HttpResponse,JsonResponse
from django.utils.crypto import get_random_string
# Create your views here.
def connect(request):
	
	if request.methode == "POST":
		user=user.connect(request.POST.get('name'),request.POST.get('password'))
		if(user!=None):
			rand=get_random_string(length=128)
			response=redirect('home')
			response.set_cookie('remember_me',rand,max_age=3600*24*10)
			userbis.add_cooki(user,rand)
			return response
		else:
			return redirect('landpage')

def deconnect(request):
	
	if 'remember_me' in request.COOKIES:
		rmcooki(request.COOKIES['remember_me'])

	response= redirect('landpage')
	response.delete_cookie('check_in')
	response.delete_cookie('remember_me')
	return response			

def history(request):
	
	pass

def objective(request):
	pass
