from utils import limpar_terminal, carregar_dados, salvar_dados
from funcionarios import adicionar_aluno, ver_alunos, excluir_aluno

arquivo_funcionarios = 'arquivos/funcionarios.txt'

# Função para login de gerente
def login_gerente():
    limpar_terminal()
    print("----------------------------------------")
    print("Login do Gerente")
    print("----------------------------------------")
    login = input("Login: ")
    senha = input("Senha: ")
    if login == "admin" and senha == "admin123":  # Credenciais fixas para o gerente
        menu_gerente()
    else:
        print("Login ou senha incorretos!")
        input("Pressione Enter para continuar...")

# Menu do gerente
def menu_gerente():
    while True:
        limpar_terminal()
        print("----------------------------------------")
        print("Menu do Gerente")
        print("----------------------------------------")
        print("1. Adicionar novo aluno")
        print("2. Ver lista de alunos")
        print("3. Excluir aluno")
        print("4. Adicionar novo funcionário")
        print("5. Ver lista de funcionários")
        print("6. Excluir funcionário")
        print("7. Voltar")
        print("----------------------------------------")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_aluno()
        elif escolha == '2':
            ver_alunos()
        elif escolha == '3':
            excluir_aluno()
        elif escolha == '4':
            adicionar_funcionario()
        elif escolha == '5':
            ver_funcionarios()
        elif escolha == '6':
            excluir_funcionario()
        elif escolha == '7':
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

# Função para adicionar novo funcionário
def adicionar_funcionario():
    limpar_terminal()
    print("----------------------------------------")
    print("Adicionar Novo Funcionário")
    print("----------------------------------------")
    login = input("Login do funcionário: ")
    senha = input("Senha do funcionário: ")
    funcionarios = carregar_dados(arquivo_funcionarios)
    funcionarios.append([login, senha])
    salvar_dados(arquivo_funcionarios, funcionarios)
    print("Funcionário adicionado com sucesso!")
    input("Pressione Enter para continuar...")

# Função para ver lista de funcionários (enumerada)
def ver_funcionarios():
    limpar_terminal()
    print("----------------------------------------")
    print("Lista de Funcionários")
    print("----------------------------------------")
    funcionarios = carregar_dados(arquivo_funcionarios)
    for i, func in enumerate(funcionarios, start=1):
        print(f"{i}. Login: {func[0]}, Senha: {func[1]}")
    print("----------------------------------------")
    input("Pressione Enter para continuar...")

# Função para excluir funcionário
def excluir_funcionario():
    limpar_terminal()
    print("----------------------------------------")
    print("Excluir Funcionário")
    print("----------------------------------------")
    funcionarios = carregar_dados(arquivo_funcionarios)
    for i, func in enumerate(funcionarios, start=1):
        print(f"{i}. Login: {func[0]}, Senha: {func[1]}")
    print("----------------------------------------")
    try:
        indice = int(input("Digite o número do funcionário que deseja excluir: ")) - 1
        if 0 <= indice < len(funcionarios):
            func_removido = funcionarios.pop(indice)
            salvar_dados(arquivo_funcionarios, funcionarios)
            print(f"Funcionário {func_removido[0]} removido com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida! Digite um número.")
    input("Pressione Enter para continuar...")