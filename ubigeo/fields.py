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
