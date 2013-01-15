# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import DisplayUbigeosForm, DetailUbigeoForm
from .models import Incident

def home(request):
    incidents = Incident.objects.all()

    if request.method == "POST":
        form = DisplayUbigeosForm(request.POST)
        if form.is_valid():
            Incident(location=form.cleaned_data['ubigeo']).save()
            return HttpResponse("A-OK")
        else:
            return render(request,
                          'index.html',
                          {'form': form,
                           'incidents': incidents,},
                          )
    else:
        form = DisplayUbigeosForm()
        return render(request,
                      'index.html',
                      {'form': form,
                       'incidents': incidents,},
                      )

def incident_detail(request, incident_id):
    incident = get_object_or_404(Incident,pk=incident_id)
    form = DetailUbigeoForm(instance=incident)
    return render(request,
        'incident_detail.html',
        {'form': form,
        'incidents': Incident.objects.all()}, )