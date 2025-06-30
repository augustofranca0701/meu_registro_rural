from django.contrib import admin
from .models import Imovel, EventoFundiario, AtividadeUsuario, AcaoUsuarioSimulada

admin.site.register(Imovel)
admin.site.register(EventoFundiario)
admin.site.register(AtividadeUsuario)
admin.site.register(AcaoUsuarioSimulada)
