from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('cms/', views.cms, name='cms'),
    path('laverne/', views.laverne, name="laverne"),
    path('chapman/', views.chapman, name="chapman"),
    path('redlands/', views.redlands, name="redlands"),
    path('callu/', views.callu, name="callu"),
    path('caltech/', views.caltech, name="caltech"),
    path('whittier/', views.whittier, name="whittier"),
    path('oxy/', views.oxy, name="oxy"),
    path('pp/', views.pp, name="pp"),
]
