from django.db import models

# Create your models here.

class Material(models.Model):
    tipoMaterial = models.CharField(max_length=200)
    codigo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    anio = models.IntegerField()
    status = models.CharField(max_length=20)

class Libro(Material):
    editorial = models.CharField(max_length=100)

class Revista(Material):
    nombre = models.CharField(max_length=100)

class Persona(models.Model):
    tipoPersona = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    numLibros = models.IntegerField()
    adeudo = models.IntegerField()

class Alumno(Persona):
    matricula = models.IntegerField()

class Profesor(Persona):
    numEmpleado = models.IntegerField()

class Prestamo(models.Model):
    codigo = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    fechaSalida = models.DateField()
    fechaRegreso = models.DateField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)