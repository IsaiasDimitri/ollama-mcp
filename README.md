## Sobre
O projeto é uma implementação de um agente local consumindo um banco de dados postgres também local.  
Escolhi o modelo qwen3:4b do ollama, que é um reasoning model, mas pode substituir por outro que seja compatível com o uso de tools.  
A lista está aqui -> https://ollama.com/search?c=tools  
Estou usando também o PydanticAI como framework para abstrair a criação do agente e o consumo do servidor MCP.

### Ambiente:
WSL: Ubuntu 22.04

### Dependências
Python >=3.12  
Docker  
Docker Compose  
Ollama  

> Crie um arquivo `.env` a partir de `.env.example` com os valores que forem convenientes.
Ao criar o banco ele usará esses valores automáticamente, e já com 100 modelos de carros cadastrados.

### Preparação
```bash
ollama pull qwen3:4b
ollama ls   # checar que foi instalado
python -m venv .venv
source .venv/bin/acticvate
pip install -r requirements.tx
```

### Execução
```bash
# cria uma rede e inicia o banco
docker network create mcp-net
docker compose up -d
python main.py  # para sair, escreva 'quit'
```
Se estiver usando o qwen3:4b e o processo de "pensar" dele estiver te irritando, inclua /no_think no seu prompt para omitir.
A qualquer momento, você pode abrir um novo terminal dar um 'attach' no banco com:
```bash
docker exec -it psql_db sh
```
e depois visualizar a tabela:
```bash
\dt cars
```