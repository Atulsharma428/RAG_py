import os
import chromadb
from langchain.vectorstores import chroma
from langchain_community.document_transformers import LongContextReorder
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings, HuggingFaceBgeEmbeddings
from langchain.retrievers.merger_retriever import MergerRetriever

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("feature-extraction", model="BAAI/bge-large-en")
# Load model directly
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-large-en")
model = AutoModel.from_pretrained("BAAI/bge-large-en")
## embedding model

model_name = "BAAI/bge-large-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}

hf = HuggingFaceBgeEmbeddings(
    model_name = model_name,
    model_kwargs = model_kwargs,
    encode_kwargs=encode_kwargs
)
print("embedding model loading...........")
