from django.urls import path
from .views import creer_facture, liste_factures, detail_facture, export_facture_pdf

urlpatterns = [
    path('creer/', creer_facture, name='creer_facture'),
    path('<int:facture_id>/export_pdf/', export_facture_pdf, name='export_facture_pdf'),
    path('<int:facture_id>/', detail_facture, name='detail_facture'),
    path('', liste_factures, name='liste_factures'),
]
