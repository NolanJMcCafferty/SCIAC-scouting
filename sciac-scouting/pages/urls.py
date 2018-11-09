from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('<team>/', views.team_view, name='team'),
    path('<team>/batters/<player>/', views.player_view, name='player'),
    path('<team>/pitchers/<pitcher>/', views.pitcher_view, name='pitcher'),
]
