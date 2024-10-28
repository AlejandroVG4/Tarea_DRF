from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuarios(AbstractUser):
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=50, default='Colombia')
    email = models.EmailField(("email address"), blank=False, unique=True)
    
    


