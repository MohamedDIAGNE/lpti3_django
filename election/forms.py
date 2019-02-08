from django.forms import ModelForm

from .models import *


class CandidatForm(ModelForm):
    class Meta:
        model = Candidat
        exclude = ['nb_voix']