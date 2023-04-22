from django.db import models

class Film(models.Model):
    isim = models.CharField(max_length=100 , default="bos")
    yil = models.IntegerField()
    tur = models.CharField(max_length=100, default="bos")
    resim_yolu = models.ImageField(upload_to='filmler/', default="bos")

class Dizi(models.Model):
    isim = models.CharField(max_length=100, default="bos")
    yil = models.IntegerField()
    tur = models.CharField(max_length=100, default="bos")
    resim_yolu = models.ImageField(upload_to='diziler/', default="bos")
