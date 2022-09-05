from urllib import response
#from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import render
#from numpy import record
import requests

# Create your views here.
def index(request):
    return render (request,'index.html')

def aboutus(request):
    return render (request,'aboutus.html')

def Contactus(request):
    return render (request,'Contactus.html')



def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    inshorts_data1 = response.json()
    records['sportsdata'] = inshorts_data1
    return render(request,'sports.html',records)

def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data2 = response.json()
    records['entertainmentdata'] = inshorts_data2
    return render(request,'entertainment.html',records)

def weather(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=weather"
    response = requests.get(url=url)
    inshorts_data3 = response.json()
    records['weatherdata'] = inshorts_data3
    return render(request,'weather.html',records)

    
def health(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=health"
    response = requests.get(url=url)
    inshorts_data4 = response.json()
    records['healthdata'] = inshorts_data4
    return render(request,'health.html',records)
   
def crime(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=crime"
    response = requests.get(url=url)
    inshorts_data6 = response.json()
    records['crimedata'] = inshorts_data6
    return render(request,'crime.html',records)
  
def nature(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=nature"
    response = requests.get(url=url)
    inshorts_data7 = response.json()
    records['naturedata'] = inshorts_data7
    return render(request,'nature.html',records)


    