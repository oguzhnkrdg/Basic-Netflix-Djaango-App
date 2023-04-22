from django.shortcuts import render, redirect, get_object_or_404
from appUser.views import Profil
from .models import Film, Dizi
from .forms import FilmEklemeFormu, DiziEklemeFormu
import random


def index(request):
   context={}
   return render(request, 'index.html', context)


def netflixPage(request,id):
   if request.user.is_authenticated:
        id = request.user.id
   else:
        id = None

   profil = Profil.objects.get(id=id)
   filmler = Film.objects.all()
   diziler = Dizi.objects.all()
   context = {
      "profil":profil,
      "filmler": filmler,
      "diziler": diziler,
      'id': id,
   }
   return render(request, 'netflix.html', context)


def film_listesi(request):
    filmler = Film.objects.all()
    context = {'filmler': filmler}
    return render(request, 'film_listesi.html', context)

def dizi_listesi(request):
    diziler = Dizi.objects.all()
    context = {'diziler': diziler}
    return render(request, 'dizi_listesi.html', context)

def film_ekle(request):
    if request.method == 'POST':
        form = FilmEklemeFormu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_listesi')
    else:
        form = FilmEklemeFormu()
    return render(request, 'film_ekle.html', {'form': form})

def dizi_ekle(request):
    if request.method == 'POST':
        form = DiziEklemeFormu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dizi_listesi')
    else:
        form = DiziEklemeFormu()
    return render(request, 'dizi_ekle.html', {'form': form})

def film_detay(request, pk):
    film = get_object_or_404(Film, pk=pk)
    context = {'film': film}
    return render(request, 'film_detay.html', context)

def dizi_detay(request, pk):
    dizi = get_object_or_404(Dizi, pk=pk)
    context = {'dizi': dizi}
    return render(request, 'dizi_detay.html', context)

def ana_sayfa(request):
    tum_filmler = list(Film.objects.all())
    tum_diziler = list(Dizi.objects.all())

    populer_filmler = random.sample(tum_filmler, min(6, len(tum_filmler)))
    gundemdeki_diziler = random.sample(tum_diziler, min(6, len(tum_diziler)))

    context = {
        'populer_filmler': populer_filmler,
        'gundemdeki_diziler': gundemdeki_diziler,
    }

    return render(request, 'netflixPage', context)