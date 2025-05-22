from django.shortcuts import render
from django.http import HttpResponse
from .forms import practicaForm


# Create your views here.
def index(request):
    return render(request, "index.html", {

    })

def servicios(request):
    return render(request, "servicios.html", {

    })
def practicas(request):
    return render(request, "practicas.html", {

    })


def contacto(request):
    if request.method == 'POST':
        form = practicaForm(request.POST)
        if form.is_valid():
            form.save()
    
    else: 
        form = practicaForm()
    return render(request, "contacto.html",{ 'form': form })

def inicio(request):
    return render(request, "inicio.html", {

    })
def registro(request):
    return render(request, "registro.html", {

    })