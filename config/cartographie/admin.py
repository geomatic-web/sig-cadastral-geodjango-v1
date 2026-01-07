from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Parcelle
# Register your models here.

@admin.register(Parcelle)
class ParcelleAdmin(LeafletGeoAdmin):
    list_display =(
        'numparcelle',
        'usage',
        'superficie',
        'proprietaire',
        'contact',
    )
search_field=('numparcelle','proprietaire')
list_filter =('usage',)