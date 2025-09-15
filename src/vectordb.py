import faiss
import numpy as np
import pickle

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatL2(dimension)
        self.vectors = []
        self.metadatas = []

    def add(self, embeddings, metadatas):
        self.index.add(np.array(embeddings).astype('float32'))
        self.metadatas.extend(metadatas)

    def save(self, path="faiss_index.pkl"):
        faiss.write_index(self.index, "faiss.index")
        with open(path, "wb") as f:
            pickle.dump(self.metadatas, f)

    def load(self, path="faiss_index.pkl"):
        self.index = faiss.read_index("faiss.index")
        with open(path, "rb") as f:
            self.metadatas = pickle.load(f)

    def search(self, query_vector, k=5):
        D, I = self.index.search(np.array([query_vector]).astype('float32'), k)
        return [self.metadatas[i] for i in I[0]]