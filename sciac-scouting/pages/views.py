from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Player, Team, Pitcher, Pitch


def home(request):
	if not request.user.is_authenticated:
		return redirect('login_view')
	teams = Team.objects.all()
	args = {
		'teams': teams,
	}
	return render(request, "home.html", args)


def team_view(request, team):
	if not request.user.is_authenticated:
		return redirect('login_view')
	players = Player.objects.filter(Team__urlname=team)
	pitchers = Pitcher.objects.filter(Team__urlname=team)
	the_team = Team.objects.filter(urlname=team)[0]
	args = {
		'players': players,
		'pitchers': pitchers,
		'team': the_team,
	}
	return render(request, "team_page.html", args)


def player_view(request, team, player):
	if not request.user.is_authenticated:
		return redirect('login_view')
	the_player = Player.objects.filter(urlname=player)[0]
	the_team = Team.objects.filter(urlname=team)[0]
	args = {
		'player': the_player,
		'team': the_team,
	}
	return render(request, "player_page.html", args)

def pitcher_view(request, team, pitcher):
	if not request.user.is_authenticated:
		return redirect('login_view')
	the_pitcher = Pitcher.objects.filter(urlname=pitcher)[0]
	the_team = Team.objects.filter(urlname=team)[0]
	pitches = Pitch.objects.filter(Pitcher__urlname=pitcher)
	sorted_pitches = sorted(pitches, key= lambda t: t.Order)
	args = {
		'pitcher': the_pitcher,
		'team': the_team,
		'pitches': sorted_pitches,
	}
	return render(request, "pitcher_page.html", args)


def login_view(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        # Redirect to home page
	        return redirect('home')
	    else:
	    	return render(request, "login.html", {'message': 'Invalid Login'})
	else:
		return render(request, "login.html", {'message': ''})


def logout_view(request):
	if request.method == "POST":
		logout(request)
		return redirect('login_view')






