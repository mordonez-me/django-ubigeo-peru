# -*- coding: utf-8 -*-

from django.shortcuts import render
from .forms import DisplayUbigeosForm

def home(request):
    form = DisplayUbigeosForm()
    return render(request,        
                  'index.html',
                  {'form': form},
                  )
