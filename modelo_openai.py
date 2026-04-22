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
    ("system", "Sos un soldado de guerra retirado, tienes que hablar en espanol y en terminos del ejercito sobre {experiencia} "),
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
with_message_history.invoke({"consulta": "Mi comida favorita es la pizza, Vos que comias en batalla ?", "experiencia": "segunda guerra mundial, batalla de stalingrado, vietnam"},
config={"configurable": {"session_id": "abc123"}},),

with_message_history.invoke({"consulta": "Que estrategia se solian usar en las trincheras", "experiencia": "segunda guerra mundial, batalla de stalingrado, vietnam"},
config={"configurable": {"session_id": "abc123"}},),

Respuesta=with_message_history.invoke({"consulta": "Recuerdas mi comida favorita ? Vos que comias en batalla ?", "experiencia": "segunda guerra mundial, batalla de stalingrado, vietnam"},
config={"configurable": {"session_id": "abc123"}},),



