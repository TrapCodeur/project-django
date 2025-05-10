from django.shortcuts import render, get_object_or_404
from .models import Championship, Team, Ranking

def championship_list(request):
    championships = Championship.objects.all()
    return render(request, 'rankings/championship_list.html', {'championships': championships})

def team_list(request, championship_id):
    championship = get_object_or_404(Championship, id=championship_id)
    teams = championship.teams.all()
    return render(request, 'rankings/team_list.html', {'championship': championship, 'teams': teams})

def ranking_list(request, championship_id):
    championship = get_object_or_404(Championship, id=championship_id)
    rankings = Ranking.objects.filter(team__championship=championship).order_by('-points', '-wins', 'losses')
    return render(request, 'rankings/ranking_list.html', {'championship': championship, 'rankings': rankings})


def championship_detail(request, championship_id):
    # Récupérer le championnat ou renvoyer une erreur 404
    championship = get_object_or_404(Championship, id=championship_id)
    # Récupérer les équipes du championnat
    teams = championship.teams.all()
    # Récupérer les classements liés au championnat
    rankings = Ranking.objects.filter(team__championship=championship).order_by('-points', '-wins', 'losses')

    return render(
        request, 
        'rankings/championship_detail.html', 
        {'championship': championship, 'teams': teams, 'rankings': rankings}
    )