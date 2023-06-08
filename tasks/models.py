from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver

type_identificacion = [
    (1, 'Seleccione'),
    (2, 'Cedula de ciudadania'),
    (3, 'Cedula de extranjeria'),
    ]
class Ingeniero(models.Model):
    def delete(self, *args, **kwargs):
        # Eliminar al usuario asociado
        if self.user:
            self.user.delete()
        
        # Eliminar al ingeniero
        super().delete(*args, **kwargs)
    Tipo_de_identificacion = models.IntegerField(
        blank=False, null=False, 
        choices=type_identificacion,
        default=1
    )   
    Identificacion = models.IntegerField()
    COD_ingeniero = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=70)
    Apellidos = models.CharField(max_length=70)
    Username = models.CharField(max_length=50, null=False, blank=False)
    Email = models.CharField(max_length=70)
    ROL = models.CharField(max_length=50) 
    Direccion = models.CharField(max_length=80)
    Telefono = models.IntegerField() 
    #user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
# Create your models here.

type_id = [
    (1, 'Seleccione'),
    (2, 'Cedula de ciudadania'),
    (3, 'Cedula de extranjeria'),
    (4, 'NIT'),
    ]

class Cliente(models.Model):
    Tipo_de_identificacion = models.IntegerField(
        blank=False, null=False, 
        choices=type_id,
        default=1
    )
    NID = models.IntegerField(primary_key=True)
    Razon_social = models.CharField(max_length=70)
    Direccion = models.CharField(max_length=70)
    Email = models.CharField(max_length=70) 
    Telefono = models.IntegerField()
   
class Proyecto(models.Model):
    Codigo = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500)
    Costo = models.FloatField(max_length=(9,2))
    #user = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, null=True,  on_delete=models.CASCADE)
    ingenieros_a_cargo = models.ForeignKey(Ingeniero, null=True,  on_delete=models.CASCADE)
    ingenieros_a_cargo = models.ManyToManyField(Ingeniero)

   
class Actividad(models.Model):
    COD_actividad = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=500)
    Costo = models.FloatField(max_length=(9,2))
    user = models.ForeignKey(User, null=True,  on_delete=models.CASCADE)
    proyecto= models.ForeignKey(Proyecto, null=True,  on_delete=models.CASCADE)
    ingeniero= models.ForeignKey(Ingeniero, null=True,  on_delete=models.CASCADE)

numeroFuentes = [
    (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10),
    (11, 11),(12, 12),(13, 13),(14, 14),(15, 15),(16, 16),(17, 17),(18, 18),(19, 19),(20, 20),
]

state = [
    (1, 'Seleccione'),
    (2, 'En proceso'),
    (3, 'Terminado')
]
type_font = [
    (1, 'Seleccione'),
    (2, 'RPG'),
    (3, 'RPGLE'),
    (4, 'RPGLE y RPG'),
    
]

workedFonts = [
    (1, 'Seleccione'),
    (2, 'RPG'),
    (3, 'RPGLE'),
]

class Bitacora(models.Model):
    Fecha = models.DateField()
    COD_bitacora = models.AutoField(primary_key=True)
    Horas_laboradas = models.FloatField(max_length=5, null=False)
    cliente = models.ForeignKey(Cliente, null=True,  on_delete=models.CASCADE)
    Proyecto= models.ForeignKey(Proyecto, null=True,  on_delete=models.CASCADE)
    Actividad= models.ForeignKey(Actividad, null=True,  on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Cantidad_de_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=numeroFuentes,
        default=1
    )
    Tipos_de_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=type_font,
        default=1
    )
    Estado_de_los_fuentes_trabajados = models.IntegerField(
        null=False, blank=False,
        choices=state,
        default=1
    )
    
    Nota = models.TextField(max_length=300, null=True, blank=True,) 
    
    
    def delete_user_on_ingeniero_delete(sender, instance, **kwargs):
        if instance.user:
            instance.user.delete()
    
    
    
    
   
