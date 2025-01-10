import requests # Importa a biblioteca requests, que é usada para realizar requisições HTTP (como GET, POST, etc.).

import json # Importa o módulo json, que permite manipular arquivos e dados no formato JSON, como salvar ou carregar arquivos JSON.

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json' # Define a URL da API de restaurantes, de onde os dados JSON serão obtidos.

response = requests.get(url) # Realiza uma requisição HTTP do tipo GET para a URL definida. O retorno da requisição é armazenado na variável response.

# Se o print abaixo der um retorno 200, então a requisição foi bem sucedida
# Se o print abaixo der um retorno 404, então a requisição não foi bem sucedida
print(response)

if response.status_code == 200: # Verifica se o código de status da requisição é 200 (sucesso). response.status_code retorna apenas o código de status (ex.: 200, 404, etc.).

    dados_json = response.json() # Extrai o conteúdo da resposta no formato JSON e o armazena na variável dados_json. Isso transforma o JSON em uma lista ou dicionário Python.

    dados_restaurante = {} #Cria um dicionário vazio que será usado para armazenar os dados organizados por restaurante.

    for item in dados_json: # Itera sobre cada elemento (objeto JSON) na lista dados_json.

        nome_do_restaurante = item['Company'] # Obtém o nome do restaurante a partir da chave 'Company' do item atual.

        # Se o nome não estiver na lista dados_restaurante, entao ele vai adicionar o item na lista
        if nome_do_restaurante not in dados_restaurante: # Se não estiver, adiciona o restaurante como uma nova chave com um valor inicial de uma lista vazia.

            dados_restaurante[nome_do_restaurante] = []
        
        dados_restaurante[nome_do_restaurante].append({ # Adiciona um dicionário com informações do item à lista correspondente ao restaurante.
            
            "item": item['Item'], # Adiciona o nome do item (prato ou produto) ao dicionário.
            "price": item['price'], # Adiciona o preço do item ao dicionário.
            "description": item['description'] # Adiciona a descrição do item ao dicionário.
        })
    else:
        print(f'O erro foi {response.status_code}') # Caso o código de status não seja 200, exibe o erro com o código recebido (ex.: 404, 500, etc.).

# Itera sobre o dicionário dados_restaurante.
for nome_do_restaurante, dados in dados_restaurante.items(): # Para cada chave (nome_do_restaurante) e seu valor associado (dados), realiza a operação de gravação de arquivo.

    # Cria uma string com o nome do arquivo JSON para o restaurante atual.
    nome_do_arquivo = f'{nome_do_restaurante}.json' # O nome do arquivo é baseado no nome do restaurante (nome_do_restaurante), com a extensão .json.

    # Abre (ou cria) um arquivo com o nome definido em nome_do_arquivo no modo de escrita ('w').
    with open(nome_do_arquivo, 'w') as arquivo_restaurante: #O arquivo aberto é representado pelo objeto arquivo_restaurante.

        # Salva os dados do restaurante atual (dados) no arquivo arquivo_restaurante no formato JSON.
        json.dump(dados, arquivo_restaurante, indent=4) # O parâmetro indent=4 é usado para formatar o JSON com indentação, tornando-o mais legível.

# print(dados_restaurante["McDonald's"]) # Imprime os dados armazenados no dicionário para o restaurante "McDonald's".