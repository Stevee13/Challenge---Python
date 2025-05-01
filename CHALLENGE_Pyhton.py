import os, time

boas_vindas = f"\nBEM VINDO AO "
hospital_name = "HOSPITAL SABARÁ"

def animação_menu(texto):
    for i in texto:
        print(f"{i}", end="", flush=True)
        time.sleep(0.2)

def menu_principal():
    print(f"""\n
1 - Agendar Consulta
2 - Exames
3 - Informações do Paciente
0 - Sair
\n| Powered by TotemAI |
    """)

def agendar_consulta():

    msg = "\nVerificando Disponibilidade"

    nome = input("Nome do paciente: ")
    idade = input("Idade do paciente: ")
    sexo = input("Sexo do paciente: ")
    cpf = input("Digite o CPF do paciente: ")
    especialidade = input("Digite a especialidade desejada: ")
    data = input("Digite a data da consulta (DD/MM/AAAA): ")
    telefone = input("Digite o telefone de contato: ")

    with open("pacientes.txt", "a") as f:
        f.write(f"{nome},{idade},{sexo},{cpf},{telefone}\n")
    with open("consulta.txt", "a") as f:
        f.write(f"{nome},{especialidade},{data}\n")
    os.system('cls' if os.name == 'nt' else 'clear')#(debug no linux :P )

    print("\nRegistro de Consulta Recebido")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    for i in range(4):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(msg)
        time.sleep(1)
        msg += "."
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nConsulta Agendada")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def exames():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Qual seu nome? ")
    
    if os.path.exists("consulta.txt"):
        with open("consulta.txt", "r") as f:
            exames = [linha.strip() for linha in f if linha.startswith(nome)]
        if exames:
            print("\nExames encontrados: ")
            for i in exames:
                print(i)
                time.sleep(2)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Nenhum exame encontrado.")
            time.sleep(2)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Arquivo de exames não encontrado.")
        time.sleep(2)
    
    exit = input("\nDigite qualquer coisa para voltar ao menu.\n")
            
def info_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')
    nome = input("Digite o nome do paciente: ")
    encontrado = False

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
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Paciente não encontrado.")
            time.sleep(2)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Arquivo de pacientes não encontrado.")
        time.sleep(2)
    
    input("\nDigite qualquer coisa para voltar ao menu.\n")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(boas_vindas)
    animação_menu(hospital_name)
    menu_principal()

    escolha = int(input("\nEscolha a ação desejada: "))
    sair_msg = "Saindo"

    if escolha == 1:
        agendar_consulta()
    elif escolha == 2:
        exames()
    elif escolha == 3:
        info_paciente()
    elif escolha == 0:
        for i in range(4):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(sair_msg)
            time.sleep(1)
            sair_msg += "."
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opção inválida, tente novamente.")
        time.sleep(2)
