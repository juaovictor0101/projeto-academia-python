import os

# Função para limpar o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funções para manipulação de arquivos
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return [linha.strip().split(',') for linha in f.readlines()]
    except FileNotFoundError:
        return []

def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        for linha in dados:
            f.write(','.join(linha) + '\n')