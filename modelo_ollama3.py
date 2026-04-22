from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

llm = OllamaLLM(model="llama3")

""" template = PromptTemplate.from_template("Cuéntame un chiste en español que tenga sentido sobre {tema}")
chain = template | llm
print(chain.invoke({"tema": "El videjuego GTA5"}))

 template = ChatPromptTemplate.from_messages([("user", "Cuéntame un chiste en español que tenga sentido sobre {tema}")])
chain = template | llm
print(chain.invoke({"tema": "El videjuego Silent hill 2 remake"})) 

template = PromptTemplate.from_template("Dime una historia de {tema} que incluya al personaje {nombre} en español")
chain = template | llm'
print(chain.invoke({"tema": "Terror", "nombre": "Harry Potter y freddy mercury"}))

respuesta = llm.invoke("El rainbow six siege es un juego competitivo ?")
print(respuesta) """

""" from langchain_core.prompts import PromptTemplate """
from langchain_core.prompts import ChatPromptTemplate
""" prompt = ChatPromptTemplate.from_messages([
    ("system", "Sos un asistente de IA, Que esta basado en la edad media, que habla espanol y que es muy divertido"),
    ("user", "{consulta}"),
])
chain = prompt | llm
respuesta = chain.invoke({"consulta": "Como puedo cultivar trigo"})
print(respuesta)
 """


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un psicologo que atiende en espanol, y se especializaa en {temas} "),
  MessagesPlaceholder(variable_name="historia"),
    ("human", "{consulta}"),
    
])

chain = prompt | llm

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="consulta",
    history_messages_key="historia",
)
with_message_history.invoke({"consulta": "Mi pelicula favorita es El efecto mariposa ", "temas": "sueño, ansiedad, pesadillas"},
config={"configurable": {"session_id": "abc123"}},),

with_message_history.invoke({"consulta": "Odio a Jack el destripador ", "temas": "sueño, ansiedad, pesadillas"},
config={"configurable": {"session_id": "abc123"}},),

Respuesta=with_message_history.invoke({"consulta": "Haceme acordar, cual es mi pelicula favorita, y a quien odio ? ya te lo dije antes ", "temas": "sueño, ansiedad, pesadillas"},
config={"configurable": {"session_id": "abc123"}},),
print(Respuesta)
 

