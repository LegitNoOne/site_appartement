from django.urls import path
from . import views

urlpatterns = [
    path('accueil',views.accueil),
    path('reservation',views.booking, name='url_liste'),
    path('reservation/<int:page>/<str:liste_memoire>/<str:premier_jour>',views.booking, name='url_liste'),
    path('formulaire/<str:premier_jour>/<str:dernier_jour>/<int:compteur>/<int:prix>/<str:nettoyage_verification>/',views.formulaire, name='formulaire'),
    path('suppression/<str:premier_jour>/<str:dernier_jour>/',views.suppression,name='suppression'),
    path('generalites',views.generalites),
    path('comment-y-arriver',views.comment_y_arriver),
    path('en-pratique',views.en_pratique),
    path('avant-de-quitter',views.avant_de_quitter),
    path('commerces-et-activites',views.commerces_et_activites),
]

