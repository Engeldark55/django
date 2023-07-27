from django.shortcuts import render, HttpResponse

# Create your views here.
def HolaMundo(req):
    return HttpResponse("HOLA DJANGO.")
