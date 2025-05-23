from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
Você é um especialista quando o assunto é carros.
Aqui, informações sobre alguns carros: {cars}

Aqui uma pergunta para ser respondida: {question}
"""

prompt = ChatPromptTemplate.from_template(template=template)
chain = prompt | model

while True:
    question = input("Pergunte (ou digite 'q' para sair): ")
    if question == 'q':
        break

    result = chain.invoke({
        "cars": [], "question": "Qual carro tem mais custo beneficio, olhando para o preço e potencia?"
    })

    print(result)

# def main():
#     print("Hello from c2s-challenge!")


# if __name__ == "__main__":
    # main()
