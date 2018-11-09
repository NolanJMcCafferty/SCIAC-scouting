from django.contrib import admin

# Register your models here.
from .models import Team, Player, Pitcher, Pitch

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Pitcher)
admin.site.register(Pitch)