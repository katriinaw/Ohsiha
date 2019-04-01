from django.shortcuts import render
import requests, json

def index(request):
    if 'hakusana' in request.POST:
        hakusana = request.POST['hakusana']
        url = "https://visittampere.fi:443/api/v1/event?tag="+hakusana+"&start_datetime=1552255200000&end_datetime=1552773600000"
        response = requests.get(url)
        tapahtumat = response.json()
        return render(request, 'etusivu.html', {
        'tapahtumalista' : tapahtumat
        })
    else:
        return render(request, 'etusivu.html', {
        })
