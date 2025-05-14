from django.db import models

# Create your models here.
class Ramal(models.Model):    
    nome_usuario = models.CharField(max_length=50, blank=True)
    nome_completo = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    nome = models.CharField(max_length=50, blank=True)
    sobrenome = models.CharField(max_length=50, blank=True)
    ramal = models.CharField(max_length=4, default='', blank=True)
    anydesk = models.CharField(max_length=10, blank=True) 
    setor = models.CharField(max_length=50, blank=True)
    
    def __str__(self) -> str:
        return self.nome_completo