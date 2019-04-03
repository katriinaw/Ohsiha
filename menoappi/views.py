from django.shortcuts import render
import requests, json
from menoappi.forms import HakuForm

def index(request):

    if request == "POST":

        form = HakuForm(request.POST or None)
        if form.is_valid():
            pass
    else:
        form = HakuForm()
    return render(request, 'etusivu.html', {
    'form':form
    })

def haku(request):
    form = HakuForm(request.POST)
    if form.is_valid():
        hakusana= form.cleaned_data.get("hakusana")
        url = "https://visittampere.fi:443/api/v1/event?tag="+hakusana+"&start_datetime=1552255200000&end_datetime=1552773600000"
        response = requests.get(url)
        tapahtumat = response.json()
        return render(request, 'tulossivu.html', {
        'tapahtumalista' : tapahtumat, 'form':form
        })
