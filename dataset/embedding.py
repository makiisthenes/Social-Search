# from langchain_openai import OpenAIEmbeddings
from openai.types import Embedding
from openai import OpenAI
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def create_embedding(text: str) -> List[Embedding]:
	"""
		This will create a vector embedding object with the given text.
		https://platform.openai.com/docs/guides/embeddings/embedding-models
	"""
	response = client.embeddings.create(
		input=text,
		model=os.getenv("OPENAI_MODEL_NAME")
	)
	embeddings = [r.embedding for r in response.embeddings]
	return embeddings[0]

