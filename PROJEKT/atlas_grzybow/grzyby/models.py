from django.db import models

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)
    jadalne = models.BooleanField(default=True)

    def __str__(self):
        return self.nazwa

class Grzyb(models.Model):
    nazwa = models.CharField(max_length=100)
    kategoria = models.ManyToManyField(Kategoria, related_name='grzyby')  
    opis = models.TextField()
    zdjecia = models.ManyToManyField('Zdjecie', related_name='grzyby') 
    utworzono = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazwa

class Zdjecie(models.Model):
    zdjecie = models.ImageField(upload_to='grzyby', verbose_name='Zdjęcie')

    def __str__(self):
        return f"Zdjęcie {self.id}"
