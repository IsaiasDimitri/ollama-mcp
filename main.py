import asyncio
import os

from pydantic_ai import Agent
from pydantic_ai.agent import AgentRunResult
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from dotenv import load_dotenv

load_dotenv(".env")


OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
model_name = os.environ.get("MODEL", "qwen3:4b")
model = OpenAIModel(
    model_name=model_name, provider=OpenAIProvider(base_url=f"{OLLAMA_URL}/v1")
)

host = os.environ.get("DB_HOST", "db")
db_name = os.environ.get("DB_NAME", "cars_db")
user = os.environ.get("DB_USER", "user")
password = os.environ.get("DB_PASSWORD", "password")
DATABASE_URL = f"postgresql://{user}:{password}@{host}:5432/{db_name}"
pgsql_server_mcp = MCPServerStdio(
    "docker",
    args=["run", "-i", "--rm", "--network", "mcp-net", "mcp/postgres", DATABASE_URL],
)

s_prompt = f"""
Você é um assistente especializado em responder perguntas com base em uma base de dados PostgreSQL que contém uma tabela chamada "cars".

O nome do banco é {db_name}.
A tabela "cars" tem os seguintes campos:
- brand (marca do carro)
- model (modelo)
- color (cor)
- engine_type (tipo de motor, ex: V6, Elétrico, etc.)
- transmission_type (tipo de câmbio, ex: Automático, Manual)
- fuel_type (tipo de combustível, ex: Gasolina, Diesel, Elétrico)

Suas instruções:

- As perguntas podem vir em outro idioma, mas no banco os dados estão em inglês.
- Sempre escreva as consultas SQL usando **sintaxe PostgreSQL**. Não use crases ( ` ). Use aspas simples para strings e aspas duplas apenas se realmente necessário.
- Sempre coloque valores de texto entre aspas simples no SQL (por exemplo: 'Automatic'). Nunca use aspas duplas para valores.
- Ao responder perguntas, seja claro, objetivo e forneça uma explicação curta do que foi encontrado.
- Quando for adequado, gere uma consulta SQL que busca a resposta na base de dados.
- Nunca invente dados: sempre consulte a tabela "cars".
- Responda em **português**.
- Se uma pergunta for ambígua, peça mais contexto de forma educada.
- Quando uma resposta exigir contagem ou agrupamento (ex: "qual combustível mais comum?"), use `GROUP BY` e `ORDER BY` no SQL.

Exemplos de comportamento esperado:

Usuário: Quantos carros vermelhos existem?
→ Você: Existem 12 carros com a cor vermelha.  
SQL: `SELECT COUNT(*) FROM cars WHERE color = 'Red';`

Usuário: Quais são os tipos de motor disponíveis?
→ Você: Os tipos de motor disponíveis são V6, V8, Elétrico, Hybrid e I4.  
SQL: `SELECT DISTINCT engine_type FROM cars;`

Seja útil, preciso e sempre baseie sua resposta na tabela `cars`."""

agent = Agent(model, system_prompt=s_prompt, mcp_servers=[pgsql_server_mcp])


async def invoke_agent(prompt: str) -> AgentRunResult:
    return await agent.run(prompt)


async def main():
    async with agent.run_mcp_servers():
        while True:
            prompt = input("Enter your prompt: ")
            if not prompt:
                print("Prompt cannot be empty.")
                continue
            if prompt.strip() in ["exit", "quit", "q"]:
                print("Exiting...")
                break
            result = await invoke_agent(prompt)
            print("-" * 12)
            print(result.output)
            print("-" * 12)


if __name__ == "__main__":
    asyncio.run(main())
