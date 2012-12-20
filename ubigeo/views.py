# -*- coding: utf-8 -*-

from django.core import serializers
from django.http import HttpResponse
from .models import Ubigeo


def provincia(request):
    provincias = Ubigeo.objects.filter(
        parent=request.GET.get('region_id')
        ).order_by('name')
    return HttpResponse(
        serializers.serialize("json",
                              provincias,
                              ensure_ascii=False),
        mimetype='application/json')


def distrito(request):
    distritos = Ubigeo.objects.filter(
        parent=request.GET.get('province_id')
        ).order_by('name')
    return HttpResponse(
        serializers.serialize("json",
                              distritos,
                              ensure_ascii=False),
        mimetype='application/json')
