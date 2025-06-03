from django.db import models


class Ram(models.Model):
    nazev = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nazev

class Vidlice(models.Model):
    nazev = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nazev

class Brzdy(models.Model):
    nazev = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nazev

class Prehazovacka(models.Model):
    nazev = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nazev

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

 