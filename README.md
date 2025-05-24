Configure locally:
``` bash
sudo apt update && sudo apt upgrade
curl https://ollama.ai/install.sh | sh              # ollama installation
ollama pull llama3.2 

curl -LsSf https://astral.sh/uv/install.sh | sh     # uv installation
uv sync
```

testing
``` bash
uv run pytest tests/
```

fontes:
anthropic mcp article:  
mcp python sdk: https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file  
mcp-lab: https://github.com/Farzad-R/mcp-lab/tree/master/mcp_crash_course  
https://github.com/Farzad-R/mcp-lab/tree/master/mcp_crash_course#-how-to-use-mcp-with-ollama  

