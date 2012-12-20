# -*- coding: utf-8 -*-

from django.db import models
from .helpers import Enumeration

class Ubigeo(models.Model):
    name = models.TextField()
    POLITICAL_DIVISION_CHOICES = Enumeration([
        (1, 'REGION', "Region"),
        (2, 'PROVINCE', "Provincia"),
        (3, 'DISTRICT', "Distrito"),
        ])

    political_division = models.PositiveSmallIntegerField(choices=POLITICAL_DIVISION_CHOICES,)
    parent = models.ForeignKey('Ubigeo', null=True)

    def __unicode__(self):
        return self.qualified_name(self)

    @property
    def human_political_division(self,):
        if self.political_division == 1:
            return u"Region"
        elif self.political_division == 2:
            return u"Provincia"
        elif self.political_division == 3:
            return u"Distrito"
        else:
            return u"No sé"

    @staticmethod
    def qualified_name(ubigeo):
        """ie. Distrito de Magdalena en la provicina de Lima en la region de Lima
        """
        if ubigeo.parent is None:
            return u"%s de %s" % (ubigeo.human_political_division,
                                  ubigeo.name,)
        else:
            return  u"%s de %s en la %s" % (ubigeo.human_political_division,
                                         ubigeo.name,
                                         Ubigeo.qualified_name(ubigeo.parent),)


    def __eq__(self, other):
        """Comparar name con name y parents
        """
        if self.name != other.name:
            return False
        elif (self.parent is None and other.parent is not None) or \
             (self.parent is not None and other.parent is None):
            return False
        elif self.parent is None:
            return True
        else:
            return self.parent == other.parent
            
    @staticmethod
    def guess_political_division_from_code(code):
        if code.pk[0:2] == "00":
            return "No idea U_U'"
        elif code.pk[2:4] == "00":
            return "Departamento"
        elif code.pk[4:6] == "00":
            return "Provincia"
        else:
            return "Distrito"

    def clean(self):
        """Don't allow null parent except when political_divison is Region
        """
        if self.parent is None and self.political_divison != 1:
            raise ValidationError("Only Regions can have no parent.")

