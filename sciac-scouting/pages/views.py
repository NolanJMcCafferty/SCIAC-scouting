from django.shortcuts import render, redirect

from .models import pages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def home(request):
	posts = pages.objects.all()
	context = {
		'pages': posts,
		'title': 'Blog Posts:'
	}
	return render(request, "home.html", context)


def cms(request):
	return render(request, "cms/cms.html", {})

def laverne(request):
	return render(request, "laverne/laverne.html", {})

def redlands(request):
	return render(request, "redlands/redlands.html", {})

def chapman(request):
	return render(request, "chapman/chapman.html", {})

def caltech(request):
	return render(request, "caltech/caltech.html", {})

def oxy(request):
	return render(request, "oxy/oxy.html", {})

def callu(request):
	return render(request, "callu/callu.html", {})

def whittier(request):
	return render(request, "whittier/whittier.html", {})

def pp(request):
	return render(request, "pp/pp.html", {})




def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# log in the user
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = AuthenticationForm()
	return render(request, "login.html", {'form': form})

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# log the user in 
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})

def logout_view(request):
	if request.method == "POST":
		logout(request)
		return redirect('home')
