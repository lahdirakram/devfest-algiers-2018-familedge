from apps.users.models import userbis

def checkuser(request):

	if 'remember_me' in request.COOKIES:
		return userbis.is_valid(request.COOKIES['remember_me'])