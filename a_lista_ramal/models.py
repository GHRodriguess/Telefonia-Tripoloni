from django.db import models

# Create your models here.
class Ramal(models.Model):    
    nome_usuario = models.CharField(max_length=50, unique=True, blank=False)
    nome_completo = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    ramal = models.CharField(max_length=4, default='')
    anydesk = models.CharField(max_length=10) 
    
    def __str__(self) -> str:
        return self.nome_completo