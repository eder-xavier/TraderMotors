import time
import requests

def buscar_automoveis_fipe(query):
    url = 'https://parallelum.com.br/fipe/api/v1/carros/marcas'
    try:
        response = requests.get(url)
        response.raise_for_status()
        marcas = response.json()
        resultados = []
        for marca in marcas:
            url_modelos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca['codigo']}/modelos"
            time.sleep(0.5) # Adiciona um atraso de 0.5 segundos
            response_modelos = requests.get(url_modelos)
            response_modelos.raise_for_status()
            modelos = response_modelos.json()['modelos']
            for modelo in modelos:
                if query.lower() in modelo['nome'].lower():
                    url_anos = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca['codigo']}/modelos/{modelo['codigo']}/anos"
                    time.sleep(0.5) # Adiciona um atraso de 0.5 segundos
                    response_anos = requests.get(url_anos)
                    response_anos.raise_for_status()
                    anos = response_anos.json()
                    for ano in anos:
                        resultados.append({
                            'marca': marca['nome'],
                            'modelo': modelo['nome'],
                            'ano': ano['nome'],
                            'codigo_fipe': ano['codigo']
                        })
        return resultados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da API FIPE: {e}")
        return []

def obter_detalhes_automovel_fipe(codigo_fipe):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/veiculo/{codigo_fipe}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar detalhes do automóvel: {e}")
        return None