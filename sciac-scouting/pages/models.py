from django.db import models
from datetime import datetime

# Create your models here.
class Team(models.Model):
	Name = models.CharField(max_length=10)
	urlname = models.CharField(max_length=20, default='none')
	color = models.CharField(max_length=20, default='white')
	Games = models.IntegerField(default=0)
	AB = models.IntegerField(default=0)
	Runs = models.IntegerField(default=0)
	Hits = models.IntegerField(default=0)
	X2B = models.IntegerField(default=0)
	X3B = models.IntegerField(default=0)
	HR = models.IntegerField(default=0)
	RBI = models.IntegerField(default=0)
	BB = models.IntegerField(default=0)
	K = models.IntegerField(default=0)
	SB = models.IntegerField(default=0)
	CS = models.IntegerField(default=0)
	AVG = models.DecimalField(decimal_places=3, max_digits=3, default=.000)
	OBP = models.DecimalField(decimal_places=3, max_digits=3, default=.000)
	SLG = models.DecimalField(decimal_places=3, max_digits=3, default=.000)	
	OPS = models.DecimalField(decimal_places=3, max_digits=4, default=.000)
	GS = models.IntegerField(default=0)
	W = models.IntegerField(default=0)
	L = models.IntegerField(default=0)
	SV = models.IntegerField(default=0)
	CG = models.IntegerField(default=0)
	H_P = models.IntegerField(default=0)
	IP = models.DecimalField(decimal_places=1, max_digits=5, default=.00)
	ER = models.IntegerField(default=0)
	BB_P = models.IntegerField(default=0)
	K_P = models.IntegerField(default=0)
	K_9_P = models.DecimalField(decimal_places=2, max_digits=3, default=.00)
	HR_P = models.IntegerField(default=0)
	ERA = models.DecimalField(decimal_places=2, max_digits=5, default=.00)
	def __str__(self):
		return self.Name

class Player(models.Model):
	Team = models.ForeignKey(Team, on_delete=models.CASCADE)
	urlname = models.CharField(max_length=50, default='')
	Name = models.CharField(max_length=50, default='')
	Position = models.CharField(max_length=10, default='')
	Year = models.CharField(max_length=20, default='Sr.')
	Games = models.IntegerField(default=0)
	AB = models.IntegerField(default=0)
	Runs = models.IntegerField(default=0)
	Hits = models.IntegerField(default=0)
	X2B = models.IntegerField(default=0)
	X3B = models.IntegerField(default=0)
	HR = models.IntegerField(default=0)
	RBI = models.IntegerField(default=0)
	BB = models.IntegerField(default=0)
	K = models.IntegerField(default=0)
	SB = models.IntegerField(default=0)
	CS = models.IntegerField(default=0)
	AVG = models.DecimalField(decimal_places=3, max_digits=3, default=.000)
	OBP = models.DecimalField(decimal_places=3, max_digits=3, default=.000)
	SLG = models.DecimalField(decimal_places=3, max_digits=3, default=.000)
	OPS = models.DecimalField(decimal_places=3, max_digits=4, default=.000)
	def __str__(self):
		return self.Name

class Pitcher(models.Model):
	Team = models.ForeignKey(Team, on_delete=models.CASCADE)
	urlname = models.CharField(max_length=50, default='')
	Name = models.CharField(max_length=50, default='')
	Hand = models.CharField(max_length=5, default='R')
	Year = models.CharField(max_length=20, default='Sr.')
	APP = models.IntegerField(default=0)	
	GS = models.IntegerField(default=0)
	W = models.IntegerField(default=0)
	L = models.IntegerField(default=0)
	SV = models.IntegerField(default=0)
	CG = models.IntegerField(default=0)
	IP = models.DecimalField(decimal_places=1, max_digits=5, default=.00)
	H = models.IntegerField(default=0)
	ER = models.IntegerField(default=0)
	BB = models.IntegerField(default=0)
	K = models.IntegerField(default=0)
	K_9 = models.DecimalField(decimal_places=2, max_digits=4, default=.00)
	HR = models.IntegerField(default=0)
	ERA = models.DecimalField(decimal_places=2, max_digits=5, default=.00)	
	def __str__(self):
		return self.Name


class Pitch(models.Model):
	class Meta:
		verbose_name_plural = "pitches"
	Pitcher = models.ForeignKey(Pitcher, on_delete=models.CASCADE)
	Type = models.CharField(max_length=50, default='')
	Velocity = models.DecimalField(decimal_places=1, max_digits=4, default=.0)
	Order = models.IntegerField(default=0)
	def __str__(self):
		return self.Pitcher.urlname + "_"  + self.Type
	









