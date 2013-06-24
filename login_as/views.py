from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, Http404

def chooser(request):
	if not request.user.is_superuser:
		raise Http404
	return render_to_response('login_as/chooser.html',
		{'users': get_user_model().objects.all()})

def login(request, user_id):
	if not request.user.is_superuser:
		raise Http404
	authed = authenticate(from_user = request.user, to_user_id = user_id)
	if not authed:
		raise Http404
	auth_login(request, authed)
	# Used as a flag that we logged in as admin
	request.session['superadmin_login'] = True
	return HttpResponseRedirect('/')