# Challenge Hospital Sabará
# TotemAI - Hospital Sabará

**TotemAI** é um sistema interativo de atendimento automatizado desenvolvido para auxiliar pacientes no Hospital Sabará.

## Funcionalidades

- **Agendar Consulta**  
  Permite ao paciente inserir seus dados e selecionar uma especialidade e data para o atendimento. As informações são registradas nos arquivos `pacientes.txt` e `consulta.txt`.

- **Exames**  
  Consulta os exames agendados com base no nome do paciente informado. Os dados são extraídos do arquivo `consulta.txt`.

- **Informações do Paciente**  
  Exibe os dados pessoais do paciente cadastrados previamente no sistema, acessando o arquivo `pacientes.txt`.

- **Cancelar Consulta**  
  Permite cancelar uma consulta agendada informando o nome do paciente. Remove o registro correspondente do arquivo `consulta.txt`.

- **Sair**  
  Encerra o sistema com uma animação de despedida.

## Validação de Dados

O sistema implementa validações para garantir a consistência dos dados inseridos:

- Nome, sexo e especialidade: apenas letras e espaços.
- Idade: apenas números.
- CPF: exatamente 11 dígitos numéricos.
- Telefone: 10 ou 11 dígitos numéricos (com DDD).
- Data: formato obrigatório `DD/MM/AAAA`.

## Estrutura dos Arquivos

- `pacientes.txt`: Armazena dados pessoais dos pacientes no formato:  
  `nome,idade,sexo,cpf,telefone`

- `consulta.txt`: Armazena os agendamentos realizados no formato:  
  `nome,especialidade,data`

## Requisitos

- Python 3.x
- Sistema Operacional com suporte a terminal/console (Windows, Linux, etc.)

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Salve o script Python em um arquivo `.py` e os arquivos `.txt` no mesmo diretório.
3. Execute o script principal pelo terminal:  
   `python nome_do_arquivo.py`

## Integrantes

- Pedro Estevam - RM 560642  
- Arthur Gomes - RM 560771  
- Luiz Gustavo - RM 560110  
- Matheus Siroma - RM 560248
