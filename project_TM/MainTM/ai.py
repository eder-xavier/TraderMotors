import tensorflow as tf
import numpy as np
from .models import Produto, ItemCarrinho

def recomendar_produtos(usuario):
    historico = ItemCarrinho.objects.filter(carrinho__usuario=usuario)
    
    if not historico:
        return Produto.objects.order_by('?')[:5]  

    produtos_ids = [item.produto.id for item in historico]

    
    produtos_array = np.array(produtos_ids).reshape(-1, 1)

    modelo = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=1000, output_dim=16),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(5, activation='softmax')
    ])

    modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Treina os dados
    modelo.fit(produtos_array, np.zeros(len(produtos_array)), epochs=5, verbose=0)

    # previsões
    recomendacoes = modelo.predict(produtos_array)

    produtos_recomendados = Produto.objects.filter(id__in=recomendacoes.flatten()[:5])
    
    return produtos_recomendados
