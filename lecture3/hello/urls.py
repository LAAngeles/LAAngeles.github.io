# es una lista de todos los allowable URLS que pueden accesar a esta aplicación
# Se crea una urlpatterns para mandar llamar al archivo views.py y se nombra a la url
# Despúes se va al archivo lecture3\urls.py para agregar la url que acabamos de crear
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
