from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Vishnu(request):
    return HttpResponse('<marquee><h1>Hii My name is Vishnu Vardhan Reddy...Iam from Banglore...</h1></marquee>')
def Anand(request):
    return HttpResponse('<h1><marquee> Anand Reddy is a Father of Vishnu Vardhan Reddy..He is Former Staying In Settipalli Penukonda Anantapuram AndharaPradesh </h1></marquee>')