# Projeto de Monitoramento Remoto de Saúde

Este projeto implementa um sistema de monitoramento remoto de saúde usando ESP32 e sensores, com armazenamento dos dados na Azure. O sistema coleta dados de pressão arterial e níveis de glicemia, enviando-os para uma API backend que armazena as informações no Azure Cosmos DB.

## Estrutura do Projeto

- **ESP32**: Código para o ESP32, responsável por coletar dados dos sensores e enviá-los para o servidor.
- **Backend**: API REST desenvolvida em Flask para receber os dados do ESP32 e armazená-los no Azure Cosmos DB.
- **Docs**: Documentação do projeto e datasheets dos sensores.
- **Tests**: Testes automatizados para o backend e o código do ESP32.

## Materiais Necessários

- **Hardware**:
  - ESP32 Development Board
  - Sensor de Pressão Arterial (ex: MPX5010DP)
  - Sensor de Glicemia (módulo comercial ou simulado)
  - Protoboard e jumpers
  - Fonte de energia para ESP32 e sensores

- **Software**:
  - Arduino IDE ou MicroPython para programar o ESP32
  - Python 3.x
  - Flask
  - Biblioteca `azure-cosmos`

- **Infraestrutura de Nuvem**:
  - Azure Cosmos DB
  - Azure App Service (opcional)

## Configuração do Ambiente

### 1. Configuração do ESP32

1. **Instale o MicroPython**: Siga as instruções [aqui](https://docs.micropython.org) para instalar o MicroPython no ESP32.
2. **Configure o Código do ESP32**: 
   - Edite o arquivo `esp32/main.py` com suas credenciais de Wi-Fi e URL do servidor.
   - Carregue o código no ESP32 usando um editor compatível com MicroPython.


