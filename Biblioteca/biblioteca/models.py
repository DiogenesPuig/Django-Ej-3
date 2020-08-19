from django.db import models

# Create your models here.

class Material(models.Model):
    tipoMaterial = models.CharField(max_length=200)
    codigo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    anio = models.IntegerField()
    status_options = [
        ('Disponible', 'Disponible'),
        ('Sin_Stock','Sin_Stock'),
    ]
    status = models.CharField(max_length=20,choices=status_options, default='Disponible')

    def __str__(self):
        return self.titulo

class Libro(Material):
    editorial = models.CharField(max_length=100)
    portada = models.ImageField(max_length=100, upload_to='img/',default='img/default.png',blank=True)

    def __str__(self):
        return 'Libro: ' + self.titulo

class Revista(Material):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return 'Revista: ' + self.titulo

class Persona(models.Model):
    tipoPersona = models.CharField(max_length=200)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    numLibros = models.IntegerField()
    adeudo = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

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

    def getTituloMaterial(self):
        return self.material.titulo

    def getNombrePersona(self):
        return self.persona.nombre