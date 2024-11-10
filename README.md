# RAG Using Python 
This repro
## Table of Contents
1. [Better RAG with Merger Retriever (LOTR) and Re-ranking Retriever (Long Context Reorder](#Better-RAG-with-Merger-Retriever-(LOTR)-and-Re-ranking-Retriever-(Long-Context-Reorder))
2. [RAGv2](#RAGv2)
3. [LangChain-RAG](#LangChain-RAG)

   
## Better RAG with Merger Retriever (LOTR) and Re-ranking Retriever (Long Context Reorder)
This project demonstrates how to use LangChain with HuggingFace embeddings, Chroma, and document loading/transforming utilities to extract embeddings and perform document retrieval. The project includes two Python files: `rag.py` and `tempcoderunner.py`.

### Prerequisites

Before running the project, ensure that you have the following dependencies installed:

- Python 3.7+
- `transformers`
- `langchain`
- `chromadb`
- `torch`
- `langchain_community`

You can install the required dependencies using the following command:

```bash 
pip install transformers langchain chromadb torch langchain_community
```
## RAGv2

### Description

RAGv2 is a state-of-the-art Retrieval-Augmented Generation model designed to enhance the capabilities of language models. It leverages a combination of retrieval and generation techniques to provide more comprehensive and informative responses to complex queries.

### How it Works

1. **Retrieval**: When presented with a query, the model first retrieves relevant information from a vast knowledge base. This information can be in the form of text, code, or other data formats.
2. **Augmentation**: The retrieved information is then augmented with the original query to provide a more comprehensive context for the generation process.
3. **Generation**: The model generates a response by combining the augmented context with its language modeling capabilities. This allows the model to produce more accurate, relevant, and informative responses.

### What it Can Do

- Answer complex questions with factual information.
- Generate creative text formats like poems, scripts, musical pieces, emails, letters, etc.
- Translate languages.
- Write different kinds of creative content.

### How to Use It

### Installation:

1. **Clone this repository**:
using this command -
```
   git clone https://github.com/Atulsharma428/RAG_py/tree/main/RAGv2
   cd RAG_py
```



## LangChain-RAG

### Description

LangChain-RAG is a powerful implementation of the Retrieval-Augmented Generation (RAG) model using LangChain. This project combines the benefits of information retrieval and advanced language models to provide more accurate, contextually rich, and informative responses to user queries. By leveraging LangChain's capabilities, this model can easily integrate with various data sources and retrieval mechanisms, making it highly flexible for different use cases.

### Features

- **Retrieval-Augmented Generation**: Combines document retrieval with language model generation for more informed responses.
- **LangChain Integration**: Uses LangChain for seamless integration with various retrieval methods and language models.
- **Customizable Pipelines**: Easily adjust and customize the retrieval and generation processes.
- **Embedding Support**: Leverage HuggingFace's pre-trained embeddings to convert documents and queries into vector representations for efficient retrieval.

### How it Works

1. **Retrieval**: The model first retrieves relevant information from a knowledge base using vector embeddings and a retriever like Chroma or another supported database.
2. **Augmentation**: The retrieved context is used alongside the original query to enhance the understanding before generating a response.
3. **Generation**: The language model generates a response using the augmented context, allowing for more relevant and accurate results.

### Installation

### Clone the Repository:

```bash
git clone https://github.com/Atulsharma428/RAG_py.git
cd RAG_py/langchain-rag
```
