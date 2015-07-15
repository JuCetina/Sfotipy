from django.shortcuts import render
from .forms import UserCreationEmailForm, EmailAuthenticationForm

from django.contrib.auth import login

def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()		

	return render(request, 'signup.html', {'form': form})

def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())
		return render(request, 'home.html', {'form': form.get_user()})

	return render(request, 'signin.html', {'form': form})

#from django.views.generic import View
#from django.http import HttpResponse


#class LoginView(View):

	#def get(self, request,*args, **kwargs):
	#	return HttpResponse('Esta es una LoginView!!!')

from django.views.generic import TemplateView, FormView
from userprofiles.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

#class LoginView(TemplateView):
class LoginView(FormView):
	template_name = 'login.html'
	#form_class = LoginForm
	success_url = '/albums'
	form_class = AuthenticationForm

	def form_valid(self, form):
		#username = form.cleaned_data['username']
		#password = form.cleaned_data['password']

		#user = authenticate(username=username, password=password)

		#login(self.request, user)

		login(self.request, form.user_cache)

		return super(LoginView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		is_auth = False
		name = None

		if self.request.user.is_authenticated():
			is_auth = True
			name = self.request.user.username

		data = {
			'is_auth': is_auth,
			'name': name,
		}

		context.update(data)

		return context

	

#class ProfileView(TemplateView):
#	template_name = 'profile.html'
#
#	def get_context_data(self, **kwargs):
#		context = super(ProfileView, self).get_context_data(**kwargs)
#
#		if self.request.user.is_authenticated():
#			context.update({'userprofile': self.get_userprofile()})
#
#		return context
#
#	def get_userprofile(self):
#		return self.request.user.userprofile		

from django.views.generic import RedirectView

class PerfilRedirectView(RedirectView):
	pattern_name = 'login'
