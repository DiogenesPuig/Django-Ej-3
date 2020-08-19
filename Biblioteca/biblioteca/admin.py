from django.contrib import admin
from biblioteca.models import *

# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('codigo','autor','titulo','status')
    list_display_links = ('codigo', 'autor', 'titulo', 'status')
    search_fields = ['autor','titulo',]

class LibroAdmin(admin.ModelAdmin):
    list_display = ('codigo','autor','titulo','editorial','status')
    list_display_links = ('codigo','autor','titulo','editorial','status')
    search_fields = ['autor','titulo','editorial']

class RevistaAdmin(admin.ModelAdmin):
    list_display = ('codigo','autor','titulo','status')
    list_display_links = ('codigo', 'autor', 'titulo', 'status')
    search_fields = ['autor','titulo',]

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','adeudo')
    list_display_links = ('nombre', 'apellido', 'adeudo')
    search_fields = ['nombre']

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'adeudo','matricula')
    list_display_links = ('nombre', 'apellido', 'adeudo', 'matricula')
    search_fields = ['nombre','matricula']

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','adeudo', 'numEmpleado')
    list_display_links = ('nombre', 'apellido', 'adeudo', 'numEmpleado')
    search_fields = ['nombre', 'numEmpleado']

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('id', 'persona', 'material')
    list_display_links = ('id', 'persona', 'material')

admin.site.register(Material,MaterialAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Revista,RevistaAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Prestamo,PrestamoAdmin)