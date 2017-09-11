# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    telephone = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)

    def __unicode__(self):
        return "{1} {0} \n {2} \n {3} \n {4}".format(self.nom, self.prenom, self.email, self.telephone, self.poste)
