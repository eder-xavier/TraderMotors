import requests

# URL base da FIPE API
FIPE_API_URL = "https://parallelum.com.br/fipe/api/v1/carros/"

def obter_veiculo_fipe(ano, marca, modelo):
    """Consulta informações de um veículo na FIPE API"""
    try:
        # Formata a URL para pegar o modelo e ano do veículo
        url = f"{FIPE_API_URL}{marca}/{modelo}/{ano}"

        # Faz a requisição para a API da FIPE
        response = requests.get(url)

        # Verifica se a resposta foi bem sucedida
        if response.status_code == 200:
            dados_veiculo = response.json()
            return dados_veiculo
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a FIPE API: {e}")
        return None
