from django.contrib import admin
from .models import Usuario, UsuarioAdmin, Rol


# Register your models here.
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol)
