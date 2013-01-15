# -*- coding: utf-8 -*-

from django import forms
from ubigeo.fields import UbigeoField
from .models import Incident

class DisplayUbigeosForm(forms.Form):
    ubigeo = UbigeoField(required=False)

class DetailUbigeoForm(forms.ModelForm):

    location = UbigeoField(required=False)
    class Meta:
        model = Incident