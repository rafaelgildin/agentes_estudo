from variables import *
from graph import graph

def stream_graph_updates(config:dict, user_input: str):
    for event in graph.stream(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config
        ):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)

config = {"configurable": {"thread_id":  thread_id}}

mensagem_index = 0
mensagens = [
    "ola",
    "quem é você?"
]

while True:
    try:
        if mensagem_index < len(mensagens):
            user_input = mensagens[mensagem_index]
        else:
            user_input = input("User: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Até mais!")
                break
        
        state = stream_graph_updates(config,user_input)

    except:
        # fallback if input() is not available
        user_input = "Como pode me ajudar hoje?"
        print("User: " + user_input)
        stream_graph_updates(config,user_input)
        break
    mensagem_index+=1
    

        

