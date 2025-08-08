from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from variables import *
import os

class State(TypedDict):
    messages: Annotated[list, add_messages]

# modelo
llm = init_chat_model("openai:gpt-4o-mini")

# chatbot
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

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