import os, time

boas_vindas = f"\nBEM VINDO AO "
hospital_name = "HOSPITAL SABARÁ"

def animação_menu(texto):
    for i in texto:
        print(f"{i}", end="", flush=True)
        time.sleep(0.2)

def validar_nome(msg):
    while True:
        nome = input(msg).strip()
        if nome.replace(" ", "").isalpha():
            return nome
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Nome inválido. Use apenas letras.")

def validar_idade():
    while True:
        idade = input("Idade do paciente: ")
        if idade.isdigit():
            return idade
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Idade deve ser um número.")

def validar_cpf():
    while True:
        cpf = input("Digite o CPF do paciente (apenas números): ")
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        os.system('cls' if os.name == 'nt' else 'clear')
        print("CPF inválido. Deve conter 11 dígitos numéricos.")

def validar_telefone():
    while True:
        telefone = input("Digite o telefone de contato: ")
        if telefone.isdigit() and 10 <= len(telefone) <= 11:
            return telefone
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Telefone inválido. Deve conter 10 ou 11 dígitos.")

def validar_texto(msg):
    while True:
        texto = input(msg).strip()
        if texto.replace(" ", "").isalpha():
            return texto
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Entrada inválida. Use apenas letras.")

def agendar_consulta():
    msg = "\nVerificando Disponibilidade"

    nome = validar_nome("Nome do paciente: ")
    idade = validar_idade()
    sexo = validar_texto("Sexo do paciente: ")
    cpf = validar_cpf()
    especialidade = validar_texto("Digite a especialidade desejada: ")
    data = input("Digite a data desejada: ")
    telefone = validar_telefone()

    try:
        with open("pacientes.txt", "a") as f:
            f.write(f"{nome},{idade},{sexo},{cpf},{telefone}\n")
        with open("consulta.txt", "a") as f:
            f.write(f"{nome},{especialidade},{data}\n")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nRegistro de Consulta Recebido")
    time.sleep(2)

    for _ in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(msg)
        time.sleep(1)
        msg += "."
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nConsulta Agendada com Sucesso!")
    time.sleep(1)

def exames():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = validar_nome("Qual seu nome? ")

    try:
        if os.path.exists("consulta.txt"):
            with open("consulta.txt", "r") as f:
                exames = [linha.strip() for linha in f if linha.startswith(nome)]
            if exames:
                print("\nExames encontrados: ")
                for i in exames:
                    print(i)
                    time.sleep(1)
            else:
                print("Nenhum exame encontrado.")
        else:
            print("Arquivo de exames não encontrado.")
    except Exception as e:
        print(f"Erro ao ler os exames: {e}")

    input("\nPressione Enter para voltar ao menu.")

def info_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = validar_nome("Digite o nome do paciente: ")
    encontrado = False

    try:
        if os.path.exists("pacientes.txt"):
            with open("pacientes.txt", "r") as f:
                for i in f:
                    if i.startswith(nome):
                        encontrado = True
                        print("\nInformações do paciente:")
                        print(i)
                        time.sleep(2)
                        break
            if not encontrado:
                print("Paciente não encontrado.")
        else:
            print("Arquivo de pacientes não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar paciente: {e}")

    input("\nPressione Enter para voltar ao menu.")

def cancelar_consulta():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite o nome do paciente para cancelar a consulta: ")

    try:
        if os.path.exists("consulta.txt"):
            with open("consulta.txt", "r") as f:
                consultas = f.readlines()

            novas_consultas = [c for c in consultas if not c.startswith(nome)]

            if len(novas_consultas) < len(consultas):
                with open("consulta.txt", "w") as f:
                    f.writelines(novas_consultas)
                print("\nConsulta cancelada com sucesso.")
            else:
                print("\nNenhuma consulta encontrada para este nome.")
        else:
            print("Arquivo de consultas não encontrado.")
    except Exception as e:
        print(f"Erro ao cancelar consulta: {e}")

    input("\nDigite qualquer coisa para voltar ao menu.\n")

# menu principal

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(boas_vindas)
    animação_menu(hospital_name)
    print(f"""\n
        1 - Agendar Consulta
        2 - Exames
        3 - Informações do Paciente
        4 - Cancelar Consulta
        0 - Sair
        \n| Powered by TotemAI |
        """)
    

    try:
        escolha = int(input("\nEscolha a ação desejada: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        time.sleep(2)
        continue

    if escolha == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        agendar_consulta()
    elif escolha == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        exames()
    elif escolha == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        info_paciente()
    elif escolha == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        cancelar_consulta()
    elif escolha == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        sair_msg = "Saindo"
        for _ in range(4):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(sair_msg)
            time.sleep(1)
            sair_msg += "."
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        print("Opção inválida, tente novamente.")
        time.sleep(2)
