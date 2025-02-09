from utils import limpar_terminal
from alunos import login_aluno
from funcionarios import login_funcionario
from gerente import login_gerente
import os


# Arquivos de dados

arquivo_alunos = 'arquivos/alunos.txt'
arquivo_funcionarios = 'arquivos/funcionarios.txt'

# Dados iniciais (se os arquivos não existirem)

if not os.path.exists(arquivo_alunos):
    with open(arquivo_alunos, 'w') as f:
        f.write('joao,1234\nmaria,5678\n')

if not os.path.exists(arquivo_funcionarios):
    with open(arquivo_funcionarios, 'w') as f:
        f.write('func1,senha1\nfunc2,senha2\n')

# Função para exibir o menu principal
def menu_principal():
    limpar_terminal()
    print("----------------------------------------")
    print("Bem-vindo ao sistema da Academia João Bombadão")
    print("----------------------------------------")
    print("1. Aluno")
    print("2. Funcionário")
    print("3. Gerente")
    print("4. Sair")
    print("----------------------------------------")
    escolha = input("Escolha uma opção: ")
    return escolha

# Loop principal do sistema
def main():
    while True:
        escolha = menu_principal()
        if escolha == '1':
            login_aluno()
        elif escolha == '2':
            login_funcionario()
        elif escolha == '3':
            login_gerente()
        elif escolha == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

# Iniciar o sistema
if __name__ == "__main__":
    main()
