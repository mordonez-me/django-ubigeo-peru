# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from .forms import DisplayUbigeosForm
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
