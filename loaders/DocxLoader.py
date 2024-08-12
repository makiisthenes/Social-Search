from langchain_community.document_loaders import Docx2txtLoader
from loaders.BaseLoader import AbstractBaseLoader
from typing import List
import glob  # OS independent file traversal.


class DocxLoader(AbstractBaseLoader):
	"""A class that loads CSV files into documents."""
	def __init__(self):
		self.all_documents = []

	def load(self, csv_file_paths: List[str]):
		raise NotImplementedError("Method not implemented yet.")


if __name__ == "__main__":
	doc_files = glob.glob("data/*.docx")
	doc_loader = DocxLoader()
	documents = doc_loader.load(doc_files)
