from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *

from .forms import CandidatForm

# Create your views here.
def liste_candidats(request):
    #Vue renvoyant à l'utilisateur la liste des candidats de l'élection
    candidats = Candidat.objects.all()
    contexte = {
        'liste' : candidats
    }
    return render(request, 'election/candidats.html', contexte)


def detail_candidat(request, id_candidat):
    #Vue renvoyant le détail d'un candidat
    candidat = get_object_or_404(Candidat, pk=id_candidat)
    return render(request, 'election/candidat.html', {'candidat' : candidat})


def ajout_candidat(request):
    #Vue permettant l'ajout d'un nouveau candidat
    if request.method == 'POST':
        form = CandidatForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/candidat/liste')
    else:
        form = CandidatForm()
        return render(request, 'election/ajout_candidat.html', {'form' : form})