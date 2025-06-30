from django.db import models
from django.utils import timezone

class Imovel(models.Model):
    nome = models.CharField(max_length=200)
    codigo_car = models.CharField(max_length=100)
    area_ha = models.DecimalField(max_digits=10, decimal_places=2)
    tem_ccir = models.BooleanField(default=True)
    tem_georreferenciamento = models.BooleanField(default=True)
    tem_reserva_legal = models.BooleanField(default=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome

class EventoFundiario(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='eventos')
    data = models.DateField()
    tipo_evento = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.tipo_evento} em {self.data}"

class AcaoUsuarioSimulada(models.Model):
    data = models.DateTimeField()
    tipo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.tipo} - {self.data}"

class AtividadeUsuario(models.Model):
    TIPO_CHOICES = [
        ('relatorio', 'Gerou relatório'),
        ('visualizou', 'Visualizou CAR'),
        ('cpf', 'Consultou CPF/CNPJ'),
        ('membro', 'Adicionou membro'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.data.strftime('%d/%m/%Y %H:%M')}"