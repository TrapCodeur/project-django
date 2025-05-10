from django.contrib import admin
from classement.models import Championship, Team, Ranking
# Register your models here.
@admin.register(Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'season')
    search_fields = ('name', 'country')
    list_filter = ('season', 'country')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'championship', 'logo')
    search_fields = ('name',)
    list_filter = ('championship',)

@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    list_display = ('team', 'played', 'wins', 'draws', 'losses', 'points')
    search_fields = ('team__name',)
    list_filter = ('team__championship',)
    ordering = ('-points', '-wins', 'losses')

