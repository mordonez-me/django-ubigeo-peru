# -*- coding: utf-8 -*-

from django import forms
from ubigeo.fields import UbigeoField
from .models import Incident


class IncidentForm(forms.ModelForm):

    location = UbigeoField(required=False)
    class Meta:
        model = Incident
