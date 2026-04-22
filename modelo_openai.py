""" from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")
respuesta = llm.invoke("El rainbow six siege es un juego competitivo ?")
print(respuesta)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente de IA, Que esta basado en la edad media, que habla espanol y que es muy divertido"),
    ("user", "{consulta}"),
])
chain = prompt | llm """

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI 

llm = ChatOpenAI(model="GPT-4o")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un psicologo que atiende a {Cosas}, y se especializaa en {Temas} ")
    ("human", "{consulta}"),
    MessagesPlaceholder(variable_name="history"),
])

chain = prompt | llm

