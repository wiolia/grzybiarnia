from django.urls import path, re_path
from django.views.static import serve
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.strona_glowna, name='strona_glowna'),
    path('lista_grzybow/', views.lista_grzybow, name='lista_grzybow'),
    path('lista_kategorii/dodaj_kategorie/', views.dodaj_kategorie, name='dodaj_kategorie'),
    path('dodaj_grzyba/', views.dodaj_grzyba, name='dodaj_grzyba'),
    path('lista_kategorii/', views.lista_kategorii, name='lista_kategorii'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
