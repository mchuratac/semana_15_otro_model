from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    rol = models.ManyToManyField(Rol, through='RolUsuario', through_fields=('usuario_id', 'rol_id'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class RolUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE,)
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Rol Usuario'
        verbose_name_plural = 'Roles Usuario'

    def __str__(self):
        return f'{self.usuario_id} / {self.rol_id}'

class RolUsuario_inline(admin.TabularInline):
    model = RolUsuario
    extra = 1

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (RolUsuario_inline,)
