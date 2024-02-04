import requests

def realizar_consulta():
    url = 'https://www.bv.com.br/simular?gclid=CjwKCAiAiP2tBhBXEiwACslfngyEZLAxeZjVLLhBGqaySoXc4CwR1uJ1mMBXA5M9wObOd-7jgcAOyBoCljgQAvD_BwE#/veiculo?idcmp=T01%7CC04%7CV03%7CF08%7CP206%7CP%7C576004913193%7Csimulador_bv_financiamento_veiculos%7Cfv_midia_google_conversao_simulador_bv_search_012022'
 
    # Parâmetros da consulta (ajuste conforme necessário)
    parametros = {'nome': nome, 'data_nascimento': data_nascimento}

    # Realiza a consulta POST
    resposta = requests.post(url, data=parametros)

    # Verifica se a requisição foi bem-sucedida (status code 200)
    if resposta.status_code == 200:
        resultado = resposta.text  # Supondo que a resposta seja em formato de texto
        # Faça o processamento do resultado conforme necessário
        with open('./Resposta.html', 'w', encoding='utf-8') as arquivo:
            arquivo.write(resultado)

        print("Resposta salva com sucesso.")

# Exemplo de uso


realizar_consulta()
