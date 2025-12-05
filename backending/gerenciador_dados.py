import json
import os

CAMINHO_ABSOLUTO = os.path.join(os.path.dirname(__file__), "Dados")

os.makedirs(CAMINHO_ABSOLUTO, exist_ok=True)

def carregar_dados(nome_arquivo):
    caminho_arquivo = os.path.join(CAMINHO_ABSOLUTO, nome_arquivo)
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump({"total": 0, "ingressos": 0, "inteira": 0, "meia": 0, "promocional": 0, "gratuita": 0}, 
            arquivo, indent=4, ensure_ascii=False) #Padronizando p/ dicionário vazio
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo) #Padronizando p/ dicionário com alguma info
    
    
    return dados


def salvar_dados(nome_arquivo, dados):
    caminho_arquivo = os.path.join(CAMINHO_ABSOLUTO, nome_arquivo)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)