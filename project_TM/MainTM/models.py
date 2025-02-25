from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nome_completo = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_completo if self.nome_completo else self.username

class Peca(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='pecas/', blank=True, null=True)
    automoveis_compatíveis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class InteracaoUsuario(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    codigo_fipe = models.CharField(max_length=50, null=True, blank=True)
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE, null=True, blank=True)
    tipo_interacao = models.CharField(max_length=50)
    data_interacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo_interacao} - {self.data_interacao}"