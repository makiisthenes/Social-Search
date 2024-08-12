# Based on the documentation mentioned here,
# https://python.langchain.com/v0.2/docs/integrations/vectorstores/faiss/
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_openai import OpenAIEmbeddings  # No need to get embedding from Social-Search.dataset.embedding
from dotenv import load_dotenv
from uuid import uuid4
from typing import List
import numpy as np
import faiss, os

load_dotenv()

embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))
index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))  # Get length of vector.


class FaissVectorDatabase:
	"""A singleton class that holds the instance of the vector database and the index object for the RAG system."""
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(FaissVectorDatabase, cls).__new__(cls)
		return cls.instance

	def __init__(self):
		"""Check if the index file exists, if not, create a new one, this will create Faiss index/vector database."""
		self.vector_store = FAISS(
		    embedding_function=embeddings,
		    index=index,
		    docstore=InMemoryDocstore(),
		    index_to_docstore_id={},
		)

	def save_index(self, index_file_path: str = "index.faiss"):
		"""Save the index to the file path."""
		faiss.write_index(self.vector_store.index, index_file_path)
		return index_file_path

	def load_index(self, index_file_path: str = "index.faiss"):
		"""Load the index from the file path."""
		self.vector_store.index = faiss.read_index(index_file_path)
		return self.vector_store.index

	def add_document(self, documents: List[Document], doc_id: str):
		"""Add a document to the vector store."""
		doc_ids = [str(uuid4()) for _ in range(len(documents))]
		self.vector_store.add_documents(documents, ids=doc_ids)

	def get_retriever(self) -> VectorStoreRetriever:
		"""Return the retriever object for use in a Langchain Expression Language (LCEL) chain."""
		return self.vector_store.as_retriever()
	