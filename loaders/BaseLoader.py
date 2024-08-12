from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from typing import List
import abc, os

# Load the environment variables
load_dotenv()


class AbstractBaseLoader(object, abc.ABC):
	def __init__(self, config=None):
		if config is None:
			config = {
				"chunk_size": os.getenv("CHUNK_SIZE"),
				"chunk_overlap": os.getenv("CHUNK_OVERLAP_SIZE"),
			}
		self.config = config
		self.splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
			chunk_size=self.config.get("chunk_size"),
			chunk_overlap=self.config.get("chunk_overlap"),
		)

	@abc.abstractmethod
	def load(self):
		raise NotImplementedError("load() method not implemented")

	def document_splitter(self, text) -> List[str]:
		"""Will split documents into different sentences."""
		chunks = self.splitter.split_text(text=text)
		return chunks
