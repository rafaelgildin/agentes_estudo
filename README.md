
# Chatbot Especialista em n8n com LangGraph

Este projeto é um agente de chatbot construído com Python, utilizando as bibliotecas LangGraph e LangChain. O agente foi projetado para atuar como um especialista em n8n do instituto IPOG, auxiliando os usuários com suas dúvidas sobre a ferramenta de automação n8n.

A aplicação oferece duas interfaces para interação: uma interface de chat baseada na web, construída com Streamlit, e uma interface de linha de comando (CLI).

## Funcionalidades

O chatbot é conversacional e com estado, o que significa que ele memoriza o histórico da conversa para uma determinada sessão. Ele é construído sobre o motor LangGraph, que define a lógica do agente como um grafo de máquina de estados, e utiliza LangChain para as interações com o modelo de linguagem.

A personalidade e a especialidade do agente são definidas através de um prompt de sistema no arquivo `src/graph.py`, o que facilita sua adaptação para outros propósitos. O projeto também inclui notebooks Jupyter para experimentação e análise do grafo.

## Estrutura do Projeto

O código-fonte principal fica na pasta `src`, que contém a aplicação Streamlit (`app.py`), a definição do grafo do agente (`graph.py`), um script para execução via terminal (`run.py`) e um arquivo para gerenciar variáveis de ambiente e IDs de sessão (`variables.py`). A pasta `notebooks` contém os arquivos para desenvolvimento e análise.

## Configuração e Uso

Para configurar o projeto, é necessário clonar o repositório, criar um ambiente virtual Python e instalar as dependências, como `langchain`, `langgraph` e `streamlit`. Também é preciso criar um arquivo `.env` para fornecer a chave da API da OpenAI.

Para executar, você pode iniciar a interface web com o comando `streamlit run src/app.py` ou usar a versão de linha de comando com `python src/run.py`.

Uma vez que a aplicação esteja em execução, você pode começar a fazer perguntas sobre o n8n. O agente se apresentará como um assistente do IPOG e responderá às suas dúvidas.