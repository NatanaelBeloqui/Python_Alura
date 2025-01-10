import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url) # Pegando todo o conteudo

print(response)

if response.status_code == 200:
    dados_json = response.json() # Convertendo para json e armazenando em uma variavel
    dados_restaurante = {} # Criando um dicionario

    for item in dados_json:
        nome_do_restaurante = item['Company'] # Pegando o nome do restaurante e armazenando em uma variavel

        # Verificar e armazenar no dicionario
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = [] # Criando uma lista para cada nome do restaurante

        dados_restaurante[nome_do_restaurante].append({'item': item['Item'],'price': item['price'],            'description': item['description']})
        for nome_do_restaurante, dados in dados_restaurante.items():
            nome_do_arquivo = f'{nome_do_restaurante}.json'
            with open(nome_do_arquivo, 'w') as arquivo_restaurante:
                json.dump(dados, arquivo_restaurante, indent=4)
        else:
            print(f'O erro foi {response.status_code}')
    