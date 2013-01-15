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

        self.fields = (
            forms.ModelChoiceField(
                queryset=Ubigeo.objects.filter(
                    political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.REGION
                    ),
                empty_label=u"",
                required=False),
            forms.ModelChoiceField(
                queryset=Ubigeo.objects.filter(
                    political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.PROVINCE
                    ),
                empty_label=u"",
                required=False),
            forms.ModelChoiceField(
                queryset=Ubigeo.objects.filter(
                    political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.DISTRICT
                    ),
                empty_label=u"",
                required=False,),
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


    def clean(self, value):
        """I know I shouldn't override this but, Fuck this shit.
        """
        if value is None:
            return None
        v1, v2, v3 = value
        if not v3 in (None, u''):
            return Ubigeo.objects.get(pk=v3)
        elif not v2 in (None, u''):
            return Ubigeo.objects.get(pk=v2)
        elif not v1 in (None, u''):
            return Ubigeo.objects.get(pk=v1)

    def compress(self, data_list):
        if data_list:
            return data_list[2]
        return None

    def prepare_value(self, value):
        if value is None:
            return None
        ubigeo = Ubigeo.objects.get(pk=value)
        provinces = Ubigeo.objects.none()
        districts = Ubigeo.objects.none()
        regions = Ubigeo.objects.filter(
                political_division=Ubigeo.POLITICAL_DIVISION_CHOICES.REGION,
                )
        if ubigeo.human_political_division == 'Region':
            provinces = Ubigeo.objects.filter(
                parent=ubigeo,
                )
        if ubigeo.human_political_division == 'Provincia':
            provinces = Ubigeo.objects.filter(
                parent=ubigeo.parent,
                )
        if ubigeo.human_political_division == 'Distrito':
            provinces = Ubigeo.objects.filter(
                parent=ubigeo.parent.parent,
                )
            districts = Ubigeo.objects.filter(
                parent=ubigeo.parent,
                )
        self.fields[1].queryset = provinces
        self.fields[2].queryset = districts
        self.widget.provinces = self.fields[1]._get_choices()
        self.widget.districts = self.fields[2]._get_choices()
        self.widget.decompress(value)
        return value
