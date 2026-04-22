from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250) 
""" Que me devuelva el mejor resultado, con un maximo de 250 caracteres """
tool = WikipediaQueryRun(api_wrapper=api_wrapper)

""" print(tool.name)
print(tool.description)
print(tool.args) 
print (tool.run("Peñarol")) """


from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

""" 
print(search.invoke("Como salio el superclasico en argentina?")) """


tools = [tool, search]
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate , HumanMessagePromptTemplate

llm = ChatOllama(model="llama3", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente de IA hecho para ayudar. Tienes acceso a herramientas para buscar información."),
    ("human", "{consulta}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

from langchain.agents import create_tool_calling_agent, AgentExecutor

agent = create_tool_calling_agent(llm, tools, prompt)

