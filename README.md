# Challenge---Python
# TotemAI - Hospital Sabará

**TotemAI** é um sistema interativo de atendimento automatizado desenvolvido para auxiliar pacientes no Hospital Sabará.

## Funcionalidades

- **Agendar Consulta**  
  Permite ao paciente inserir seus dados e selecionar uma especialidade e data para o atendimento. As informações são registradas nos arquivos `pacientes.txt` e `consulta.txt`.

- **Exames**  
  Consulta os exames agendados com base no nome do paciente informado. Os dados são extraídos do arquivo `consulta.txt`.

- **Informações do Paciente**  
  Exibe os dados pessoais do paciente cadastrados previamente no sistema, acessando o arquivo `pacientes.txt`.

- **Sair**  
  Encerra o sistema com uma animação de despedida.

## Estrutura dos Arquivos

- `pacientes.txt`: Armazena dados pessoais dos pacientes (nome, idade, sexo, CPF, telefone).
- `consulta.txt`: Armazena os agendamentos realizados (nome do paciente, especialidade, data).

## Requisitos

- Python 3.x
- Sistema Operacional com suporte a terminal/console (Windows, Linux, etc.)

## Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone ou baixe o repositório com o código-fonte.
3. Execute o script principal.
