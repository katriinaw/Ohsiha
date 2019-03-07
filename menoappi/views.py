from django.shortcuts import render
import requests, json

def index(request):
    response = requests.get('https://visittampere.fi:443/api/v1/event?tag=viihde&start_datetime=1552255200000&end_datetime=1552773600000')
    tapahtumat = response.json()
    return render(request, 'etusivu.html', {
    'id' : tapahtumat[0]['title']

    #response = requests.get('https://fineli.fi/fineli/api/v1/foods/11049')
    #ravintosisalto = response.json()
    #return render(request, 'etusivu.html', {
    #'hiilarit' : ravintosisalto['carbohydrate']
    #})
