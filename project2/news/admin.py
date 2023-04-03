from django.contrib import admin

from .models import Postagens

@admin.register(Postagens)
class Personadmin(admin.ModelAdmin):
    list_filter = ["titulo"]
    search_fields = ["titulo", "conteudo"]