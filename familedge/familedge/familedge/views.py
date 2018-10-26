from django.shortcuts import render
from apps.users.models import userbis
from .functions import checkuser 
def landpage(request):

	# if checkuser(request)!=None:
	# 		return redirect('home')

	return render(request,'index.html')
