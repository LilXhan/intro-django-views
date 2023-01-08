from django.db import models

# Create your models here.

# Tener en cuenta que un modelo es una clase, por ende hay reglas que seguir
# El nombre de mi clase inicia siempre en mayuscula
# Esta clase debe heredar de models.Model

class Person(models.Model):
    
    # id = models.AutoField(primary_key=True) -> En la ultima version de django, este campo se crea automaticamente
    
    # Especificar los atributos de mi clase
    
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_two = models.CharField(max_length=200, default='')
    reference = models.CharField(max_length=200, default='')
    salary = models.FloatField(default=0.0)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + self.address




class PersonProxy(Person):
    class Meta:
        proxy = True

    def get_full_name(self):
        return self.name + " " + self.address

    def get_full_name_and_email(self):
        return self.name + " " + self.address + " " + self.email


class ValidationPersonProxy(Person):
    class Meta:
        proxy = True

    def checkpassword(self):
        if len(self.password) < 8:
            return False
        else:
            return True


# ----------- Insertar un dato a la db ---------------
# from myapp.models import Person
# p = Person(name="Flavio", email="example@gmail.com", username="flavito")
# p.save()


# ---------- Como se usa un modelo proxy -------------
# from myapp.models import PersonProxy
# p = PersonProxy.objects.get(pk=1).get_full_name()
# print(p) -> Juan Calle 1
# p2 = PersonProxy.objects.get(pk=1).get_full_name_and_email() 
# print(p2) -> Juan Calle 1 example@gmail.com
