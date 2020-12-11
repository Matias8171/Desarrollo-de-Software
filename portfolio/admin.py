from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
# Agregar contenidos a las tablas de la administracion Django, Filtros.
    readonly_fields =('created','update')
    list_display =('title','created','update','link')
    search_fields =('title','descripcion')
    date_hierarchy='created'
    list_filter =('title',date_hierarchy)
admin.site.register(Project,ProjectAdmin)
