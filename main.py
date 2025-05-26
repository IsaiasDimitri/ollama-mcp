import asyncio
import os

from pydantic_ai import Agent
from pydantic_ai.agent import AgentRunResult
from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

host = os.environ.get("DB_HOST", "localhost")
db_name = os.environ.get("DB_NAME", "cars_db")
user = os.environ.get("DB_USER", "user")
password = os.environ.get("DB_PASSWORD", "password")
DATABASE_URL = f"postgresql://{user}:{password}@{host}:5432/{db_name}"

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
model_name = os.environ.get("MODEL", "qwen3:4b")
model = OpenAIModel(
    model_name=model_name, provider=OpenAIProvider(base_url=f"{OLLAMA_URL}/v1")
)

pgsql_server_mcp = MCPServerStdio(
    "docker",
    args = [
        "run",
        "-i",
        "--rm",
        "mcp/postgres",
        DATABASE_URL
    ]
)

agent = Agent(
    model,
    mcp_servers=[pgsql_server_mcp]
)   


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
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
