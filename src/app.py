import streamlit as st
from graph import graph
from langchain_core.messages import HumanMessage, AIMessage
from variables import *

st.set_page_config(page_title="Chatbot Ipog", page_icon="🤖")
st.title("Chatbot Ipog")

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = thread_id

# --- Sidebar ---
st.sidebar.title("Opções")
if st.sidebar.button("Nova Conversa"):
    st.session_state.messages = []
    st.session_state.thread_id = thread_id
    st.rerun()
st.sidebar.text(f"ID: {st.session_state.thread_id}")

# --- Display Chat History ---
for message in st.session_state.messages:
    role = "assistant" if message.type == "ai" else "user"
    with st.chat_message(role):
        st.markdown(message.content)

text_input = st.chat_input("Digite sua mensagem")

# --- Main Logic: React to user input ---
if text_input:
    
    # Add user message to chat history and display it
    user_message = HumanMessage(content=text_input)
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        st.markdown(text_input)

    # Display assistant response
    
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        config = {"configurable": {"thread_id": st.session_state.thread_id}}
        graph_input = {"messages": [user_message]}
        
        try:
            # Call the graph to get the response
            with st.spinner("Pensando..."):
                response = graph.invoke(graph_input, config)
            
            assistant_response = response["messages"][-1]
            assistant_response_text = assistant_response.content
            
            # Display the text response
            message_placeholder.markdown(assistant_response_text)
            st.session_state.messages.append(assistant_response)
            
        except Exception as e:
            # Display the text response      
            error_message_content = "Ocorreu um erro ao processar sua mensagem. Por favor, tente novamente."
            assistant_response = AIMessage(error_message_content)
            assistant_response_text = assistant_response.content
            
            message_placeholder.markdown(assistant_response_text)
            # message_placeholder.error(error_message)
            st.session_state.messages.append(assistant_response)