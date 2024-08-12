from langchain_community.document_loaders import PyPDFLoader
from loaders.BaseLoader import AbstractBaseLoader
from typing import List
import glob  # OS independent file traversal.


class PDFLoader(AbstractBaseLoader):
	"""A class that loads PDF files into documents."""
	def __init__(self):
		self.all_documents = []

	def load(self, csv_file_paths: List[str]):
		raise NotImplementedError("Method not implemented yet.")


if __name__ == "__main__":
	pdf_files = glob.glob("data/*.pdf")
	pdf_loader = PDFLoader()
	documents = pdf_loader.load(pdf_files)
