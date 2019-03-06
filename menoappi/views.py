from django.shortcuts import render
import requests

def index(request):
    return render(request, 'etusivu.html', {})
    #response = requests.get('https://fineli.fi/fineli/api/v1/foods/11049')
    #ravintosisalto = response.json()
    #return render(request, 'etusivu.html', {
    #'hiilarit' : ravintosisalto['carbohydrate']
    #})
