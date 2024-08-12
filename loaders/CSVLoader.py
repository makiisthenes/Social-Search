from langchain_community.document_loaders import CSVLoader
from loaders.BaseLoader import AbstractBaseLoader
from typing import List
import glob  # OS independent file traversal.


class CSVFileLoader(AbstractBaseLoader):
	"""A class that loads CSV files into documents."""
	def __init__(self):
		self.all_documents = []

	def load(self, csv_file_paths: List[str]):
		print(f'Loading CSV file from {len(csv_file_paths)}')
		for csv_file_path in csv_file_paths:
			csv_loader = CSVLoader(csv_file_path)
			self.all_documents.extend(csv_loader.load())
		print(f'Loaded {len(self.all_documents)} documents from CSV files.')
		return self.all_documents


if __name__ == "__main__":
	csv_files = glob.glob("data/*.csv")
	csv_loader = CSVFileLoader()
	documents = csv_loader.load(csv_files)