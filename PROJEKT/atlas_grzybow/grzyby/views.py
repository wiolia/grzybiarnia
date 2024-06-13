from django.shortcuts import render, redirect
from .models import Kategoria, Grzyb
from .forms import GrzybForm, KategoriaForm

def strona_glowna(request):
    return render(request, 'strona_glowna.html')

def dodaj_kategorie(request):
    if request.method == 'POST':
        form = KategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('strona_glowna')
        else:
            print(form.errors)  
    else:
        form = KategoriaForm()
    return render(request, 'dodaj_kategorie.html', {'form': form})

def dodaj_grzyba(request):
    if request.method == 'POST':
        form = GrzybForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_grzybow')
    else:
        form = GrzybForm()
    
    return render(request, 'dodaj_grzyba.html', {'form': form})

def lista_kategorii(request):
    kategorie = Kategoria.objects.all()
    return render(request, 'lista_kategorii.html', {'kategorie': kategorie})

def lista_grzybow(request):
    grzyby = Grzyb.objects.all()  
    return render(request, 'lista_grzybow.html', {'grzyby': grzyby})

