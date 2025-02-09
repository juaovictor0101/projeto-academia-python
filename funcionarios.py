from utils import limpar_terminal, carregar_dados, salvar_dados

arquivo_alunos = 'arquivos/alunos.txt'
arquivo_funcionarios = 'arquivos/funcionarios.txt'

# Função para login de funcionário
def login_funcionario():
    limpar_terminal()
    print("----------------------------------------")
    print("Login do Funcionário")
    print("----------------------------------------")
    login = input("Login: ")
    senha = input("Senha: ")
    funcionarios = carregar_dados(arquivo_funcionarios)
    for func in funcionarios:
        if func[0] == login and func[1] == senha:
            menu_funcionario()
            return
    print("Login ou senha incorretos!")
    input("Pressione Enter para continuar...")

# Menu do funcionário
def menu_funcionario():
    while True:
        limpar_terminal()
        print("----------------------------------------")
        print("Menu do Funcionário")
        print("----------------------------------------")
        print("1. Adicionar novo aluno")
        print("2. Ver lista de alunos")
        print("3. Excluir aluno")
        print("4. Voltar")
        print("----------------------------------------")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_aluno()
        elif escolha == '2':
            ver_alunos()
        elif escolha == '3':
            excluir_aluno()
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

# Função para adicionar novo aluno
def adicionar_aluno():
    limpar_terminal()
    print("----------------------------------------")
    print("Adicionar Novo Aluno")
    print("----------------------------------------")
    login = input("Login do aluno: ")
    senha = input("Senha do aluno: ")
    alunos = carregar_dados(arquivo_alunos)
    alunos.append([login, senha])
    salvar_dados(arquivo_alunos, alunos)
    print("Aluno adicionado com sucesso!")
    input("Pressione Enter para continuar...")

# Função para ver lista de alunos (enumerada)
def ver_alunos():
    limpar_terminal()
    print("----------------------------------------")
    print("Lista de Alunos")
    print("----------------------------------------")
    alunos = carregar_dados(arquivo_alunos)
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. Login: {aluno[0]}, Senha: {aluno[1]}")
    print("----------------------------------------")
    input("Pressione Enter para continuar...")

# Função para excluir aluno
def excluir_aluno():
    limpar_terminal()
    print("----------------------------------------")
    print("Excluir Aluno")
    print("----------------------------------------")
    alunos = carregar_dados(arquivo_alunos)
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. Login: {aluno[0]}, Senha: {aluno[1]}")
    print("----------------------------------------")
    try:
        indice = int(input("Digite o número do aluno que deseja excluir: ")) - 1
        if 0 <= indice < len(alunos):
            aluno_removido = alunos.pop(indice)
            salvar_dados(arquivo_alunos, alunos)
            print(f"Aluno {aluno_removido[0]} removido com sucesso!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida! Digite um número.")
    input("Pressione Enter para continuar...")