from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    #organiza os campos
    list_display = ("id", "nome", "legeda", "publicada")
    #add link
    list_display_links = ("id", "nome")
    #add busca
    search_fields = ("nome",)
    list_filter = ("categoria","usuario")
    list_editable = ("publicada",)
    #quebra de página
    list_per_page = 2
    
    


admin.site.register(Fotografia, ListandoFotografias)
