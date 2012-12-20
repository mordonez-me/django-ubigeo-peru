# -*- coding: utf-8 -*-

from django import forms
from ubigeo.fields import UbigeoField

class DisplayUbigeosForm(forms.Form):
    ubigeos = UbigeoField()
