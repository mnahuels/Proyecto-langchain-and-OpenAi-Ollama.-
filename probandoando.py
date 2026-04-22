
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")
respuesta = llm.invoke("Tengo hambre, que dirias que me haga de cenar, son las 22:27 hrs")
# print(respuesta)
