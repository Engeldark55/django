from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(req):
    return render(req, 'index.html')
def Contactame(req):
    return render(req, 'Contactame.html')
def RedesSociales(req):
    return render(req,'RedesSociales.html')
