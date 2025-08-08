from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from variables import *
import os

class State(TypedDict):
    messages: Annotated[list, add_messages]

# modelo
llm = init_chat_model("openai:gpt-4o-mini")


# chatbot
def chatbot(state: State):
    """
    Invokes the agent with the current state to generate a response.
    """
    prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Você é um expert em n8n do instituto IPOG.
Sempre se apresente inicialmente de com o assistente do IPOG.
Seu objetivo é de auxiliar o usuário quanto à  aprendizagem no n8n.
Tire qualquer dúvida relevante sobre esse assunto.
Caso o usuário solicite algo diferente, responda de maneira delicada, que não consegue fazer o que foi solicitado.
            
            """,
        ),
        ("placeholder", "{messages}"),
    ]
    )
    
    # The chain combines the prompt and the model
    chain: Runnable = prompt | llm
    
    # We pass the entire message history to the chain
    response = chain.invoke({"messages": state["messages"]})
    
    # The result is a new message that we add to the state
    return {"messages": [response]}


graph_builder = StateGraph(State)

# adiciona nós
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# compilando
memory = InMemorySaver()
graph = graph_builder.compile(checkpointer=memory)

# visualizando
print('concluido')