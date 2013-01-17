# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .forms import DisplayUbigeosForm, DetailUbigeoForm
from .models import Incident

def home(request):
    incidents = Incident.objects.all()

    if request.method == "POST":
        form = DisplayUbigeosForm(request.POST)
        if form.is_valid():
            incident = Incident(location=form.cleaned_data['ubigeo'])
            incident.save()
            return redirect(
                reverse('incident_detail',
                        kwargs={'incident_id': incident.pk, }))
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
        'index.html',
        {'form': form,
        'incidents': Incident.objects.all()}, )
