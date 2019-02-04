from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Conseil(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Electeur(models.Model):
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=50)
    numero_cni = models.CharField(max_length=15)
    a_vote = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bureau = models.ForeignKey("Bureau", on_delete=models.CASCADE)
    candidat = models.ForeignKey("Candidat", on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_cni


class Candidat(models.Model):
    parti = models.CharField(max_length=100)
    date_naissance = models.DateField()
    slogan = models.CharField(max_length=100)
    programme = models.TextField()
    nb_voix = models.IntegerField(default=0)

    def __str__(self):
        return self.parti


class Bureau(models.Model):
    nom = models.CharField(max_length=255)
    lieu = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
