from utils import limpar_terminal, carregar_dados, salvar_dados

arquivo_alunos = 'arquivos/alunos.txt'

# Função para login de aluno
def login_aluno():
    limpar_terminal()
    print("----------------------------------------")
    print("Login do Aluno")
    print("----------------------------------------")
    login = input("Login: ")
    senha = input("Senha: ")
    alunos = carregar_dados(arquivo_alunos)
    for aluno in alunos:
        if aluno[0] == login and aluno[1] == senha:
            escolher_treino()
            return
    print("Login ou senha incorretos!")
    input("Pressione Enter para continuar...")

# Função para escolher o treino
def escolher_treino():
    while True:
        limpar_terminal()
        print("----------------------------------------")
        print("Escolha o Treino")
        print("----------------------------------------")
        print("1. Treino A")
        print("2. Treino B")
        print("3. Treino C")
        print("4. Voltar")
        print("----------------------------------------")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            exibir_treino('A')
        elif escolha == '2':
            exibir_treino('B')
        elif escolha == '3':
            exibir_treino('C')
        elif escolha == '4':
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")

# Função para exibir o treino escolhido
def exibir_treino(tipo):
    limpar_terminal()
    print(f"----------------------------------------")
    print(f"Treino {tipo}")
    print(f"----------------------------------------")
    if tipo == 'A':
        print("Ombros:")
        print("- Elevação lateral: 3x12")
        print("- Desenvolvimento com halteres: 3x10")
        print("Peito:")
        print("- Supino reto: 4x10")
        print("- Crucifixo: 3x12")
        print("Tríceps:")
        print("- Tríceps corda: 3x15")
        print("- Francês: 4x10")
    elif tipo == 'B':
        print("Costas:")
        print("- Barra fixa: 3x10")
        print("- Remada curvada: 4x8")
        print("Bíceps:")
        print("- Rosca direta: 3x12")
        print("- Rosca martelo: 3x12")
        print("Abdômen:")
        print("- Abdominal crunch: 3x20")
        print("- Prancha: 3x30 segundos")
    elif tipo == 'C':
        print("Pernas:")
        print("- Agachamento livre: 4x10")
        print("- Leg press: 3x12")
        print("Panturrilhas:")
        print("- Elevação de panturrilha: 4x15")
        print("- Panturrilha no leg press: 3x20")
        print("Glúteos:")
        print("- Afundo: 3x12")
        print("- Elevação pélvica: 4x10")
    print("----------------------------------------")
    input("Pressione Enter para voltar...")