# -*- coding: utf-8 -*-

from django import forms
from django.db import models
from django.forms import ModelChoiceField
from django.core.exceptions import ValidationError
from widgets import UbigeoWidget
from models import Ubigeo
import constant


class UbigeoField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        regions = Ubigeo.objects.filter(political_division=1)
        if regions:
            provinces = Ubigeo.objects.filter(parent=regions[0])
            districts = Ubigeo.objects.filter(parent=provinces[0])

        self.fields = (
            forms.ModelChoiceField(queryset=regions),
            forms.ModelChoiceField(queryset=provinces),
            forms.ModelChoiceField(queryset=districts),)

        self.widget = UbigeoWidget(
            self.fields[0]._get_choices(),
            self.fields[1]._get_choices(),
            self.fields[2]._get_choices(),
            )
        super(UbigeoField, self).__init__(
            self.fields,
            self.widget,
            *args)

    def compress(self, data_list):
        if data_list:
            return data_list[-1]
        return None
