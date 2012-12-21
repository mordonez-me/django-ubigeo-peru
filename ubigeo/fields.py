# -*- coding: utf-8 -*-

from django import forms
from .widgets import UbigeoWidget
from .models import Ubigeo


class UbigeoField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        regions = Ubigeo.objects.filter(
            political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.REGION
            )
        provinces = Ubigeo.objects.none()
        districts = Ubigeo.objects.none()

        # if regions:
        #     provinces = Ubigeo.objects.filter(parent=regions[0])
        #     districts = Ubigeo.objects.filter(parent=provinces[0])
        # else:
        #     provinces = Ubigeo.objects.none()
        #     districts = Ubigeo.objects.none()

        self.fields = (
            forms.ModelChoiceField(
                queryset=Ubigeo.objects.filter(
                    political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.REGION
                    )),
            forms.ModelChoiceField(
                queryset=Ubigeo.objects.filter(
                    political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.PROVINCE
                    )),
            forms.ModelChoiceField(
                queryset=Ubigeo.objects.filter(
                    political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.DISTRICT
                    )),
            )


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
        """Returns a single value for the given list of values.
        The values can be assumed to be valid.
        """
        if data_list:
            return data_list[-1]
        return None
