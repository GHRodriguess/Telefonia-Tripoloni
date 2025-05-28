from django.db import models

class Linha(models.Model):
    nome_usuario = models.CharField(max_length=50, blank=True)
    nome_completo = models.CharField(max_length=50, blank=True)
    numero = models.CharField(max_length=16, blank=True)
    pacote_dados_mb = models.PositiveIntegerField(help_text="Tamanho do pacote de dados em MB", default=0, blank=True)
    setor = models.CharField(max_length=50, blank=True)
    obra = models.CharField(max_length=50, blank=True)
    imprimir = models.BooleanField(default=False, help_text="Marque para imprimir o número")
    
    def pacote_formatado(self):
        if self.pacote_dados_mb >= 1024:
            return f"{self.pacote_dados_mb / 1024:.2f} GB"
        return f"{self.pacote_dados_mb} MB"