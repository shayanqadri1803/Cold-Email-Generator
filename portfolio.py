import pandas as pd
import uuid
import chromadb

class Portfolio:
    def __init__(self, file_path="your-projects-path.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.data.columns = self.data.columns.str.strip()  # Clean column names
        if "Skills" not in self.data.columns:
            raise ValueError("The 'Skills' column is missing from the CSV file.")
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=row["Skills"],
                    metadatas={"name": row["Project Name"], "description": row["Description"]},
                    ids=[str(uuid.uuid4())]
                )
                print('New Vectordb created')

    def query_descriptions(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])
  