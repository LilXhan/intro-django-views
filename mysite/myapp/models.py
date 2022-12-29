from django.db import models

# Create your models here.

# Tener en cuenta que un modelo es una clase, por ende hay reglas que seguir
# El nombre de mi clase inicia siempre en mayuscula
# Esta clase debe heredar de models.Model

class Person(models.Model):
    
    # Especificar los atributos de mi clase
    
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
