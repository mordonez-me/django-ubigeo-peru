# -*- coding: utf-8 -*-

from django.forms import widgets
from .models import Ubigeo


class UbigeoWidget(widgets.MultiWidget):

    def __init__(self, regions, provinces, districts):
        self.regions = regions
        self.provinces = provinces
        self.districts = districts
        _widgets = (
            widgets.Select(
                choices = self.regions,
            ),
            widgets.Select(
                choices = Ubigeo.objects.none(),
            ),
            widgets.Select(
                choices = Ubigeo.objects.none(),
            )
        )
        super(UbigeoWidget, self).__init__(_widgets)

    def decompress(self, value):
        if value:
            ubigeo = value if isinstance(value, Ubigeo) else Ubigeo.objects.get(
                ubigeo = value
                )
            self.widgets[1] = widgets.Select(
                choices=((u[0], u[1]) for u in self.provinces),
                )
            self.widgets[2] = widgets.Select(
                choices = ((u[0], u[1]) for u in self.districts))
            return (ubigeo.parent.parent,
                ubigeo.parent,
                ubigeo)
        return (None, None, None)

    class Media:
        js=(
            'js/jquery.js',
            'js/ubigeo.js',
        )
