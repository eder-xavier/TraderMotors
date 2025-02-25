from sklearn.neighbors import NearestNeighbors
from .utils import obter_dados_interacao_automoveis, preparar_dados_para_modelo # Importe as funções de utils.py

def treinar_modelo_recomendacao():
    """
    Treina um modelo de recomendação de automóveis usando filtragem colaborativa baseada em KNN.

    Retorna:
        tuple: Uma tupla contendo o modelo KNN treinado e a matriz de interações usuário-item.
    """
    df_interacoes = obter_dados_interacao_automoveis()
    matriz_usuario_item = preparar_dados_para_modelo(df_interacoes)
    modelo_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    modelo_knn.fit(matriz_usuario_item.values)
    return modelo_knn, matriz_usuario_item