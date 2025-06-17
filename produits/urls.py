from django.urls import path
from .views import liste_produits
from .views import add_produit
from .views import post_produit

urlpatterns = [
    path('', liste_produits, name='liste_produits'),
    path('add/', add_produit, name='add_produit'),
    path('post/', post_produit, name='post_produit'),
]
