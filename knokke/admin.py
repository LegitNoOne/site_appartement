from django.contrib import admin
from .models import Prix, reduction, Annee, Calendrier, Nettoyage, Mois
admin.site.register(Prix)
admin.site.register(reduction)
admin.site.register(Mois)
admin.site.register(Annee)
admin.site.register(Nettoyage)
admin.site.register(Calendrier)
# Register your models here.
