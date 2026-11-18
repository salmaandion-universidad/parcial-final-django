from django.contrib import admin
from .models import Profile, Programa

# Register your models here.
admin.site.register(Profile)


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'facultad', 'estado')
    search_fields = ('codigo', 'nombre', 'facultad')