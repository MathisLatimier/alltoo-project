from django.urls import path
from .views import liste_produits, add_produit, post_produit, delete_produit, edit_produit

urlpatterns = [
    path('', liste_produits, name='liste_produits'),
    path('add/', add_produit, name='add_produit'),
    path('post/', post_produit, name='post_produit'),
    path('delete/<int:produit_id>/', delete_produit, name='delete_produit'),
    path('edit/<int:produit_id>/', edit_produit, name='edit_produit'),
]
