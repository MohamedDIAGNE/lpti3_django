from django.urls import path

from .views import *

app_name="election"

urlpatterns = [
    path("candidat/liste", liste_candidats, name="liste_candidats"),
    path("candidat/detail/<int:id_candidat>", detail_candidat, name="detail_candidat"),
    path("candidat/ajout", ajout_candidat, name="ajout_candidat"),
]
