# -*- coding: utf-8 -*-

from django.forms import widgets
from .models import Ubigeo


class UbigeoWidget(widgets.MultiWidget):

    def __init__(self, regions, provinces, districts,
                 attrs_1=None, attrs_2=None, attrs_3=None, ):
        self.regions = regions
        self.provinces = provinces
        self.districts = districts
        _widgets = (
            widgets.Select(
                choices = self.regions,
                attrs=attrs_1,
            ),
            widgets.Select(
                choices = Ubigeo.objects.none(),
                attrs=attrs_2,
            ),
            widgets.Select(
                choices = Ubigeo.objects.none(),
                attrs=attrs_3,
            )
        )
        super(UbigeoWidget, self).__init__(_widgets)

    def decompress(self, value):
        if value:
            ubigeo = value if isinstance(value, Ubigeo) else Ubigeo.objects.get(
                pk = value
                )
            self.widgets[1] = widgets.Select(
                choices=((u[0], u[1]) for u in self.provinces),
                )
            self.widgets[2] = widgets.Select(
                choices = ((u[0], u[1]) for u in self.districts))
            if ubigeo.human_political_division == 'Region':
                return (ubigeo.id,
                    None,
                    None)
            if ubigeo.human_political_division == 'Provincia':
                return (ubigeo.parent.id,
                    ubigeo.id,
                    None)
            if ubigeo.human_political_division == 'Distrito':
                return (ubigeo.parent.parent.id,
                    ubigeo.parent.id,
                    ubigeo.id)
        return (None, None, None)

    class Media:
        js=(
            'js/jquery.js',
            'js/ubigeo.js',
        )
