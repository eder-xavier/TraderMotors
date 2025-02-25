# utils.py
import pandas as pd
from .models import InteracaoUsuario

def obter_dados_interacao_automoveis():
    interacoes = InteracaoUsuario.objects.filter(codigo_fipe__isnull=False).values('usuario_id', 'codigo_fipe')
    df_interacoes = pd.DataFrame.from_records(interacoes)
    return df_interacoes

def preparar_dados_para_modelo(df_interacoes):
    matriz_usuario_item = pd.crosstab(df_interacoes['usuario_id'], df_interacoes['codigo_fipe'])
    return matriz_usuario_item