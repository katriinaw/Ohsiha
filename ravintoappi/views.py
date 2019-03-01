from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'etusivu.html', {})

    #response = requests.get('https://fineli.fi/fineli/api/v1/foods/4019') #fineli tietokannasta kuoritun banaanin (elintarvike id=4019) ravintosisältö
    #geodata = response.json()
    #return render(request, 'core/home.html', {
    #    'ip': geodata['ip'],
    #    'country': geodata['country_name']
    #})
